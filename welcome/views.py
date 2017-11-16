import os
import smtplib

import boto3
from authy.api import AuthyApiClient
from botocore.exceptions import ClientError
from django.conf import settings
from django.contrib.auth.models import User
from django.core import mail
from django.db import connections
from django.db.utils import OperationalError
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from welcome.forms import WelcomeForm
from welcome.utils import check_users, check_aws_utils


def home(request, options=None):
    """
    Welcome page for new setup.

    Parameters
    ----------
    request: object
        WSGI request.
    options: str
        Defaults to None.

    Returns
    -------
    render: object
        Returns renderer's.

    """

    template = 'welcome/welcome.html'
    context = {}

    if not check_users():

        if options is None:

            if request.method == 'POST':
                form = WelcomeForm(request.POST)
                if form.is_valid():
                    first_name = form.cleaned_data.get('first_name')
                    last_name = form.cleaned_data.get('last_name')
                    username = form.cleaned_data.get('username')
                    email = form.cleaned_data.get('email')
                    password = form.cleaned_data.get('first_name')

                    user_model, created = User.objects.create_superuser(username=username, email=email,
                                                                        password=password, first_name=first_name,
                                                                        last_name=last_name)
                    if created:
                        user_model.save()
            else:
                form = WelcomeForm()

            context['form'] = form
    else:
        return redirect('portal_home')

    return render(request, template, context)


# JSON objects

def check_db_conn(request):
    """
    Checks connection to 'default' database.

    Parameters
    ----------
    request: object
        WSGI request.

    Returns
    -------
    reachable : dict
        A dictionary of bool and if not error message.
    """

    conn = connections['default']
    reachable = {}

    try:
        c = conn.cursor()  # this will take some time if error
    except OperationalError as e:
        reachable['expression'] = False
        reachable['error'] = str(e)
    else:
        reachable['expression'] = True

    return JsonResponse(reachable)


def check_ssl(request):
    """
    Checks if the connection is secured.

    Parameters
    ----------
    request: object
        WSGI request.

    Returns
    -------
    secured : dict
        A dictionary of bool and if not error message.
    """

    secured = {}
    http_response = HttpRequest()

    _secured = http_response.is_secure()

    if not _secured:
        secured['expression'] = False
        secured['error'] = "This connection is not secured, you can still continue but I would'nt recommend it."
    else:
        secured['expression'] = True

    return JsonResponse(secured)


def check_authy(request):
    """
    Checks if authy key is added and works.

    Parameters
    ----------
    request: object
        WSGI request.

    Returns
    -------
    reachable : dict
        A dictionary of bool and if not error message.
    """
    reachable = {}
    authy_api = AuthyApiClient(settings.AUTHY_API)
    stats = authy_api.apps.fetch()
    if stats.ok():
        reachable['expression'] = True
    else:
        reachable['expression'] = False
        reachable['error'] = stats.errors()

    return JsonResponse(reachable)


def check_smtp(request):
    """
    Checks if SMTP connection is possible or not.

    Parameters
    ----------
    request: object
        WSGI request.

    Returns
    -------
    reachable : dict
        A dictionary of bool and if not error message.
    """
    reachable = {'expression': False}

    try:
        user = User.objects.get(id=1)
    except User.DoesNotExist as e:
        reachable['expression'] = False
        reachable['error'] = str(e)
        return JsonResponse(reachable)

    try:
        # TODO: Ask user to give a default email ID in app.json
        mail.send_mail("Checking SMTP", "Test email for checking SMTP.", "test@" + settings.SHARE_URL, [user.email])
        reachable['expression'] = True
    except smtplib.SMTPException as e:
        reachable['expression'] = False
        reachable['error'] = str(e)

    return JsonResponse(reachable)


def check_aws(request):
    """
    Checks for AWS connection.

    Parameters
    ----------
    request: object
        WSGI request.

    Returns
    -------
    reachable : dict
        A dictionary of bool and if not error message.
    """

    reachable = {}

    session = boto3.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', 'a'),
                            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', 'a'))
    s3 = session.client('s3')
    try:
        response = s3.list_buckets()
    except ClientError as e:
        reachable['expression'] = False
        reachable['error'] = str(e)
    else:
        reachable['expression'] = True

    return JsonResponse(reachable)


def check_aws_s3(request):
    """
    Once ``check_aws`` returns true, this will check for the required S3 bucket.

    Parameters
    ----------
    request: object
        WSGI request.

    Returns
    -------
    available: dict
        A dictionary of bool and if not error message.
    """

    session = boto3.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', 'a'),
                            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', 'a'))
    s3 = session.client('s3')
    available = {'expression': False}

    if check_aws_utils():
        for bucket_list in s3.list_buckets()['Buckets']:
            if bucket_list['Name'] == settings.AWS_STORAGE_BUCKET_NAME:
                available['expression'] = True
                break

    return JsonResponse(available)
