import datetime
import logging

import phonenumbers
from authy.api import AuthyApiClient
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import (User)
from django.contrib.auth.views import login as auth_login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.views.decorators.cache import never_cache

from .forms import LoginForm, AuthyForm, AuthenticatorModelForm, MobileCheckerForm
from .models import AuthenticatorModel
from .utils import get_user_from_sid, has_2fa, get_uuid_json

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

    session_key = request.session.session_key

    user_id = get_user_from_sid(session_key)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        data = 'console.log("Not authorised")'
        response = HttpResponse('console.log("Not authorised")', content_type='application/javascript')
        return response

    users = User.objects.all()

    context = {'users': users}

    return render(request, template, context, content_type='application/javascript')


def user(request):
    """
    Users page.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.

    """
    template = 'user/index.html'

    session_key = request.session.session_key

    user_id = get_user_from_sid(session_key)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login')

    context = {}

    return render(request, template, context)


def two_fa_home(request):
    """
    Two-Factor authentication home page.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.

    """

    template = 'user/2fa/index.html'

    session_key = request.session.session_key

    user_id = get_user_from_sid(session_key)

    try:
        _user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login')

    try:
        _auth = AuthenticatorModel.objects.get(id=user_id)
        if _auth.authy_id is None:
            return redirect('2fa_register')
    except AuthenticatorModel.DoesNotExist:
        return redirect('2fa_register')

    context = {'user': _user, 'auth': _auth}

    return render(request, template, context)


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
                return redirect('2fa_auth')
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
        if request.get_signed_cookie('is_personal', salt=str(user_auth.session_id)) == 'yes':
            return redirect('/admin/')

    authy_api = AuthyApiClient(settings.AUTHY_API)

    template = 'user/2fa/auth.html'
    if request.GET.get('sms') == 'yes':
        sms = authy_api.users.request_sms(user_auth.authy_id, {'force': True})
        if sms.ok():
            context['sms'] = True
        else:
            context['sms'] = sms.errors()['message']

    if request.method == 'POST':
        form = AuthyForm(request.POST)
        if form.is_valid():

            # Checks if the entered token is a backup code.
            token = request.POST.get('authy', None)
            if '-' in token:
                logger.info('Could be backup code')
                content = {}
                uuids = user_auth.uuids['uuid']
                if token in uuids:
                    logger.info('Backup code found')
                    data = uuids.index(token)
                    uuids[data] = '*'
                    content['uuid'] = uuids
                    AuthenticatorModel.objects.filter(id=1).update(uuids=content)
                    logger.info('Backup code replaced.')
                    return redirect('/admin/')

            # Checks using Authy's code.
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


def two_fa_register(request):
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
    template = "user/2fa/2fa_register.html"

    session_key = request.session.session_key
    user_id = get_user_from_sid(session_key)
    try:
        _user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login')

    try:
        auth = AuthenticatorModel.objects.get(id=1)
        if auth.authy_id is not None:
            return redirect('2fa_home')
        elif auth.authy_id is None and auth.phone_number is not None:

            phone_number = phonenumbers.parse(str(auth.phone_number))

            logger.info('User: "' + _user.username + '" phone number found but not Authy ID, forwarding to '
                                                     '"confirm_mobile".')

            authy_api = AuthyApiClient(settings.AUTHY_API)
            authy_mobile = authy_api.phones.verification_start(phone_number.national_number,
                                                               phone_number.country_code, via='sms')

            return redirect('confirm_mobile')
    except AuthenticatorModel.DoesNotExist:
        pass

    logger.info('User: "' + _user.username + '" registering for 2FA')

    if request.method == "POST":
        form = AuthenticatorModelForm(request.POST)

        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone_number = request.POST.get('phone_number')
            email_id = request.POST.get('email_id')

            authenticator_model, created = AuthenticatorModel.objects.update_or_create(id=1,
                                                                                       user_id=_user,
                                                                                       first_name=first_name,
                                                                                       last_name=last_name,
                                                                                       phone_number=phone_number,
                                                                                       email_id=email_id)
            if created:
                request.session['phone_number'] = str(phone_number)
                phone_number = phonenumbers.parse(str(phone_number))

                authenticator_model.save()

                # Create unique session ID.
                unique_id = get_random_string(length=32)
                AuthenticatorModel.objects.filter(id=1).update(session_id=unique_id, uuids=get_uuid_json())

                logger.info('User: "' + _user.username + '" redirected to confirm phone number.')

                authy_api = AuthyApiClient(settings.AUTHY_API)
                authy_mobile = authy_api.phones.verification_start(phone_number.national_number,
                                                                   phone_number.country_code, via='sms')

                if authy_mobile.ok():
                    return redirect('confirm_mobile')
                else:
                    print(authy_mobile.errors())

    else:
        form = AuthenticatorModelForm()

    context = {'form': form, 'user': _user}

    return render(request, template, context)


def delete_auth(request):
    """
    Deletes Authy user.

    Returns
    -------
    content: str
        Conformation string.
    """

    session_key = request.session.session_key
    user_id = get_user_from_sid(session_key)
    try:
        _user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login')

    try:
        auth_model = AuthenticatorModel.objects.get(id=1)
        logger.info('No 2FA registered, redirecting to 2FA registration area.')
    except AuthenticatorModel.DoesNotExist:
        return redirect('2fa_register')

    if auth_model.authy_id is not None:
        authy_api = AuthyApiClient(settings.AUTHY_API)

        authy_user = authy_api.users.delete(auth_model.authy_id)

        # if authy_user.errors():
        #     return _user.errors()['message']

    auth_model.delete()
    logger.info('User: "' + _user.username + '" removed 2FA')

    return redirect('2fa_register')


def confirm_mobile(request):
    """
    Confirm mobile number before creating an Authy account.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.
    """
    template = "user/2fa/confirm_mobile.html"

    try:
        auth = AuthenticatorModel.objects.get(id=1)
        if auth.authy_id is not None:
            return redirect('2fa_home')
    except AuthenticatorModel.DoesNotExist:
        pass

    if request.method == 'POST':
        form = MobileCheckerForm(request.POST)

        if form.is_valid():
            auth_code = request.POST.get('auth_code')
            authy_api = AuthyApiClient(settings.AUTHY_API)

            phone_number = phonenumbers.parse(request.session.get('phone_number'))

            authy_mobile = authy_api.phones.verification_check(phone_number.national_number, phone_number.country_code,
                                                               int(auth_code))

            if authy_mobile.ok():
                auth_model_data = AuthenticatorModel.objects.get(id=1)
                authy_user = authy_api.users.create(str(auth_model_data.email_id), phone_number.national_number,
                                                    phone_number.country_code)
                AuthenticatorModel.objects.filter(id=1).update(authy_id=str(authy_user.id))

                del request.session['phone_number']
                request.session.modified = True

                return redirect('2fa_home')

    else:
        form = MobileCheckerForm()

    context = {'form': form}

    return render(request, template, context)


def log_me_out(request):
    """
    Logout user and clear all the cookies.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.

    """
    logout(request)
    response = redirect('login')
    response.delete_cookie('is_personal')
    return response
