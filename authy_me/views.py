import logging

from django.contrib.auth import authenticate, login
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import (User)
from django.contrib.auth.views import login as auth_login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.cache import never_cache

from .forms import LoginForm
from .models import AuthenticatorModel

logger = logging.getLogger(__name__)


def get_user_auth(request):
    user = get_user(request)

    if user.is_authenticated():
        return user
    else:
        return user


@never_cache
def users_js(request):
    """
        Returns a `user` JavaScript for Authenticator model.

        Parameters
        ----------
        request: WSGIRequest
            WSGI request.

        Returns
        -------
        render: HttpResponse
            Returns renderer's.

        """
    template = 'js/users.js'

    users = User.objects.all()

    context = {'users': users}

    return render(request, template, context, content_type='text/javascript')


def log_me_in(request):
    """
    Checks if the user is staff and if he/she doesn't have 2FA enabled, this view forces them to create one. If the
    staff has a 2FA, then this view redirects the user to authenticate them.

    Parameters
    ----------
    request: WSGIRequest

    Returns
    -------
    auth_login: object

    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            if user.is_staff and not has_2fa(user):
                logger.info('is staff but does not have 2FA, redirecting to Authy account creator')
                login(request, user)
                return redirect('/admin/authy_me/authenticatormodel/')
            elif user.is_staff and has_2fa(user):
                logger.info("is staff and 2FA enabled redirecting to Authy verification")
                return redirect('2fa')
            elif not request.user.is_staff and not has_2fa(user):
                logger.info('is not staff and does not have 2FA')

    defaults = {
        'authentication_form': LoginForm,
        'template_name': 'login.html',
    }

    return auth_login(request, **defaults)


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


def auth_2fa(request):
    if request.user.is_authenticated():
        print('yes')

    return HttpResponse('hello')
