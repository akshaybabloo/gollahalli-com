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

from .forms import LoginForm, AuthyForm, AuthenticatorModelForm
from .utils import get_user_from_sid, has_2fa
from .models import AuthenticatorModel

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
    session_key = request.session.session_key

    user_id = get_user_from_sid(session_key)

    try:
        user = User.objects.get(id=user_id)
        return redirect('/admin/')
    except User.DoesNotExist:
        pass

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
                if request.POST.get('remember_me'):
                    request.session.set_expiry(31557600)
                return redirect('2fa')
            else:
                logger.info('is not staff and does not have 2FA')
                return redirect('/')

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

    context = {}
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

    authy_api = AuthyApiClient(settings.AUTHY_API)

    template = 'security/2fa/auth.html'
    if request.GET.get('sms') == 'yes':
        sms = authy_api.users.request_sms(user_auth.authy_id, {'force': True})
        if sms.ok():
            context['sms'] = True
        else:
            context['sms'] = sms.errors()['message']

    if request.method == 'POST':
        form = AuthyForm(request.POST)
        if form.is_valid():
            token = request.POST.get('authy', None)
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

    context['form'] = form

    return render(request, template, context)


def auth_2fa_register(request):
    """
    Registration form for 2FA.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.

    """
    template = "security/2fa/2fa_register.html"

    session_key = request.session.session_key

    user_id = get_user_from_sid(session_key)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login')

    form = AuthenticatorModelForm()

    if request.method == "POST":
        form = AuthenticatorModelForm(request.POST)

        if form.is_valid():
            id = request.POST.get('id')
            user_id = request.POST.get('user_id')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone_number = request.POST.get('phone_number')
            email_id = request.POST.get('email_id')
            authy_id = request.POST.get('authy_id')
            session_id = request.POST.get('session_id')

            authenticator_model, created = AuthenticatorModel.objects.update_or_create(id=id, user_id=user_id,
                                                                                       first_name=first_name,
                                                                                       last_name=last_name,
                                                                                       phone_number=phone_number,
                                                                                       email_id=email_id,
                                                                                       authy_id=authy_id,
                                                                                       session_id=session_id)
            if created:
                authenticator_model.save()

    context = {'form': form}

    return render(request, template, context)
