import datetime
import logging

import phonenumbers
from authy.api import AuthyApiClient
from django.conf import settings
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.models import (User)
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.views.decorators.cache import never_cache

from gollahalli_cms.authy_me.forms import LoginForm, AuthyForm, AuthenticatorModelForm, MobileCheckerForm, ChangePasswordForm
from gollahalli_cms.authy_me.models import AuthenticatorModel
from gollahalli_cms.authy_me.utils import get_user_from_sid, has_2fa, get_uuid_json

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
        _user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        response = HttpResponse('console.log("Not authorised")', content_type='application/javascript')
        return response

    users = User.objects.all()

    context = {'users': users}

    return render(request, template, context, content_type='application/javascript')


def two_fa_home(request, options):
    """
    Two-Factor authentication home page.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.
    options: str
        Optional strings.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.

    """

    template = 'portal/user/2fa/2fa_index.html'

    if request.user.is_anonymous:
        return redirect('login')

    try:
        _user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        return redirect('login')

    try:
        _auth = AuthenticatorModel.objects.get(user_id=request.user)
        if _auth.authy_id is None:
            return redirect('2fa_register')
    except AuthenticatorModel.DoesNotExist:
        return redirect('2fa_register')

    if options == 'reset_backup_codes':
        # Create unique session ID.
        unique_id = get_random_string(length=32)
        AuthenticatorModel.objects.filter(id=1).update(session_id=unique_id, uuids=get_uuid_json())

    context = {'user': _user, 'auth': _auth}

    return render(request, template, context)


class CustomLoginView(LoginView):
    """
    Custom login view.
    """

    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.is_staff and has_2fa(self.request):
            return redirect('{}'.format(self.request.GET.get('next', 'portal_home')))

        return super(CustomLoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):

        if self.request.user.is_staff and not has_2fa(self.request):
            logger.info('is staff but does not have 2FA, redirecting to Authy account creator')
            auth_login(self.request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
            return redirect('2fa_register')

        return super(CustomLoginView, self).form_valid(form)


def log_me_in(request):
    """
    Checks if the user is staff and if he/she doesn't have 2FA enabled, this view forces them to create one. If the
    staff has a 2FA, then this view redirects the user to authenticate them.

    Parameters
    ----------
    request: object
        Django request.

    Returns
    -------
    auth_login: object
        Renders template.

    """

    # Check if user already logged in.
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('{}'.format(request.GET.get('next', 'portal_home')))

    context = {}
    defaults = {
        'authentication_form': LoginForm,
        'template_name': 'login.html',
    }

    if request.user.is_anonymous is False:
        logout(request)
        context['error'] = 'For security reason your previous session has expired. Please login again.'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        _user = authenticate(username=username, password=password)

        if _user is not None and _user.is_active:
            if _user.is_staff and not has_2fa(_user):
                logger.info('is staff but does not have 2FA, redirecting to Authy account creator')
                auth_login(request, _user)
                return redirect('2fa_register')

            elif _user.is_staff and has_2fa(_user):
                logger.info("is staff and 2FA enabled redirecting to Authy verification")

                if request.POST.get('remember_me'):
                    request.session.set_expiry(31557600)

                is_personal_cookie_exist = request.COOKIES.get('is_personal', None)
                if is_personal_cookie_exist is not None:
                    response = redirect('2fa_auth')
                    response.delete_cookie('is_personal')
                    return response

                request.session['auth'] = _user.id
                return redirect('2fa_auth')
            else:
                logger.info('is not staff and does not have 2FA')
                return redirect('/')

    return auth_login(request, extra_context=context, **defaults)


def auth_2fa(request):
    """
    Authenticates the user using Authy's 2-factor authentication. If the user checked the tick box to save the
    authentication then a cookie is set and expires after one year.

    Parameters
    ----------
    request: object
        Request.
    """
    user_id = request.session.get('auth', None)

    context = {}

    _user = User.objects.get(id=user_id)
    user_auth = _user.auth_user.get(id=user_id)

    if 'is_personal' in request.COOKIES:
        if request.get_signed_cookie('is_personal', salt=str(user_auth.session_id)) == 'yes':
            return redirect('{}'.format(request.GET.get('next')))

    authy_api = AuthyApiClient(settings.AUTHY_API)

    template = 'portal/user/2fa/auth.html'
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
                    _user = authenticate(request, username=_user.username, password=_user.password)
                    auth_login(request, _user)
                    response = redirect('portal_home')
                    max_age = 365 * 24 * 60 * 60  # one year
                    expires = datetime.datetime.strftime(
                        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                        "%a, %d-%b-%Y %H:%M:%S GMT")
                    response.set_signed_cookie('is_personal', 'yes', salt=str(user_auth.session_id), expires=expires)
                    return response
                _user = authenticate(request, username=_user.username, password=_user.password)
                auth_login(request, _user)
                return redirect('portal_home')
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
    template = "portal/user/2fa/2fa_register.html"

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
    template = "portal/user/2fa/confirm_mobile.html"

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


def profile_home(request):
    """
    Profile homepage.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.

    """
    session_key = request.session.session_key

    user_id = get_user_from_sid(session_key)

    try:
        _user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('login')

    template = 'portal/user/profile/profile_index.html'

    # Change password
    pwd_msg = ''
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            current_pwd = request.POST.get('current_password')
            new_pwd = request.POST.get('password')

            if _user.check_password(str(current_pwd)):
                _user.set_password(str(new_pwd))
                logger.info("Password changed.")
                pwd_msg = 'Password successfully changed'
            else:
                form.add_error(None, 'The password you have entered did not match in our system')
    else:
        form = ChangePasswordForm()

    context = {'pwd': form, 'pwd_msg': pwd_msg}

    return render(request, template, context)
