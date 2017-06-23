import datetime
import logging

from authy.api import AuthyApiClient
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import (User)
from django.contrib.auth.views import login as auth_login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.cache import never_cache

from .forms import LoginForm, AuthyForm
from .utils import get_user_from_sid, has_2fa

logger = logging.getLogger(__name__)


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
                login(request, user)
                return redirect('2fa')
            elif not request.user.is_staff and not has_2fa(user):
                logger.info('is not staff and does not have 2FA')

    defaults = {
        'authentication_form': LoginForm,
        'template_name': 'login.html',
    }

    return auth_login(request, **defaults)


def auth_2fa(request):
    """
    Authenticates the user using Authy's 2-factor authentication. If the user checked the tick box to save the
    authentication then a cookie is set and expires after one year.

    Parameters
    ----------
    request: WSGIRequest
        Request.
    """
    session_key = request.session.session_key

    user_id = get_user_from_sid(session_key)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login')

    user_auth = user.auth_user.get(id=user.id)

    if 'is_personal' in request.COOKIES:
        if request.get_signed_cookie('is_personal', salt='#c}jbb9j>c.oMKP=T)M.3%fe') == 'yes':
            return redirect('/admin/')

    template = 'auth.html'
    if request.method == 'POST':
        form = AuthyForm(request.POST)
        if form.is_valid():
            token = request.POST.get('authy', None)
            authy_api = AuthyApiClient(settings.AUTHY_API)
            verification = authy_api.tokens.verify(user_auth.authy_id, str(token))
            if verification.ok():
                if request.POST.get('is_personal') == 'on':
                    response = redirect('/admin/')
                    max_age = 365 * 24 * 60 * 60  # one year
                    expires = datetime.datetime.strftime(
                        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                        "%a, %d-%b-%Y %H:%M:%S GMT")
                    response.set_signed_cookie('is_personal', 'yes', salt='#c}jbb9j>c.oMKP=T)M.3%fe', expires=expires)
                    return response
                return redirect('/admin/')
            else:
                form.add_error(None, verification.errors()['message'])
    else:
        form = AuthyForm()

    context = {'form': form}

    return render(request, template, context)
