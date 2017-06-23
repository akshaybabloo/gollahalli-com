from django.conf import settings
from django.contrib.auth.models import (User)
from django.utils.module_loading import import_module

from .models import AuthenticatorModel


def is_int(s):
    """
    Checks if the content is of type int or not.

    Parameters
    ----------
    s: int
        Input should be integer type.

    Returns
    -------
    bool: bool
        Returns True is the input is of type integer else returns False.

    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def has_2fa(request):
    """
    Checks if `AuthenticatorModel` is associated with `User` model.

    Returns
    -------
    content: bool
        Returns True is if `AuthenticatorModel` is associated with `User` else returns False.
    """

    content = True

    try:
        user = User.objects.get(username=request.username)
    except User.DoesNotExist:
        content = False
        pass

    try:
        user_auth = user.auth_user.get(id=user.id)
    except AuthenticatorModel.DoesNotExist:
        content = False
        pass

    return content


def get_user_from_sid(session_key):
    """
    Returns users id bassed on the session.

    Parameters
    ----------
    session_key: str
        User session key.

    Returns
    -------
    uid: int
        Users id.
    """
    django_session_engine = import_module(settings.SESSION_ENGINE)
    session = django_session_engine.SessionStore(session_key)
    uid = session.get('_auth_user_id')
    return uid
