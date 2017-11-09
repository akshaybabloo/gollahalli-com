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
from django.http import HttpRequest


def check_users():
    """
    Checks if the CMS has any user and at least one of them is a staff.

    Returns
    -------
    has_n_staff: bool
        Has users and at least one of them is a staff.

    """
    has_n_staff = False

    try:
        users = User.objects.all()

        for user in users:
            if user.is_staff:
                has_n_staff = True
    except User.DoesNotExist:
        return has_n_staff

    return has_n_staff


def check_db_conn():
    """
    Checks connection to 'default' database.

    Returns
    -------
    reachable : bool
        True if BD connects else False.
    """

    conn = connections['default']

    try:
        c = conn.cursor()  # this will take some time if error
    except OperationalError:
        reachable = False
    else:
        reachable = True

    return reachable


def check_ssl():
    """
    Checks if the connection is secured.

    Returns
    -------
    secured : bool
        True if secured else False.
    """

    http_response = HttpRequest()

    secured = http_response.is_secure()

    return secured


def check_authy():
    """
    Checks if authy key is added and works.

    Returns
    -------
    reachable : bool
        True if connected else False.
    """

    authy_api = AuthyApiClient(settings.AUTHY_API)
    stats = authy_api.apps.fetch()
    if stats.ok():
        return True
    else:
        return False


def check_smtp():
    """
    Checks if SMTP connection is possible or not.

    Returns
    -------
    reachable : bool
        True if connected else False.
    """
    reachable = False

    try:
        user = User.objects.get(id=1)
    except User.DoesNotExist:
        return reachable

    try:
        mail.send_mail("Checking SMTP", "Test email for checking SMTP.", "test@" + settings.SHARE_URL, [user.email])
        reachable = True
    except smtplib.SMTPException:
        reachable = False

    return reachable


def check_aws():
    """
    Checks for AWS connection.

    Returns
    -------
    reachable : bool
        True if connected else False.
    """

    session = boto3.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', 'a'),
                            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', 'a'))
    s3 = session.client('s3')
    try:
        response = s3.list_buckets()
    except ClientError:
        reachable = False
    else:
        reachable = True

    return reachable


def check_aws_s3():
    """
    Once ``check_aws`` returns true, this will check for the required S3 bucket.

    Returns
    -------
    available: bool
        True if bucket available else False.
    """

    session = boto3.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', 'a'),
                            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', 'a'))
    s3 = session.client('s3')
    available = False

    if check_aws():
        for bucket_list in s3.list_buckets()['Buckets']:
            if bucket_list['Name'] == settings.AWS_STORAGE_BUCKET_NAME:
                available = True
                break

    return available
