from django.contrib.auth.models import User
from django.db.utils import OperationalError
from django.db import connections


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
