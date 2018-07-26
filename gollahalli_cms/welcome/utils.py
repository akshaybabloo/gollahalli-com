import os

import boto3
from botocore.exceptions import ClientError
from django.contrib.auth.models import User


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
                break
        return has_n_staff
    except User.DoesNotExist:
        return has_n_staff


def check_aws_utils():
    """
    Checks for AWS connection.

    Parameters
    ----------
    request: object
        WSGI request.

    Returns
    -------
    reachable : bool
        True if connected to AWS else False.
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
