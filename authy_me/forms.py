import logging

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _

from .models import AuthenticatorModel
from .utils import is_int

logger = logging.getLogger(__name__)


class AuthenticatorAdminForm(forms.ModelForm):
    """
    AuthenticatorModel form for admin view.
    """

    authy_id = forms.CharField(widget=forms.NumberInput, required=False,
                               help_text='This ID is provided by Authy and cannot be changed.')
    session_id = forms.CharField(required=False, help_text='This field is auto generated.')

    class Meta:
        model = AuthenticatorModel
        fields = '__all__'

    class Media:
        js = ('//code.jquery.com/jquery-3.2.1.min.js',
              'js/users.js',)


class AuthenticatorModelForm(forms.Form):
    """
    AuthenticatorModel form.
    """

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=50)
    email_id = forms.EmailField()

    def clean(self):

        cd = self.cleaned_data

        if cd.get('phone_number') is None:
            raise forms.ValidationError(_("Phone number is required."))

        if cd.get('first_name') is None:
            raise forms.ValidationError(_("First name is required."))

        if cd.get('last_name') is None:
            raise forms.ValidationError(_("Last name is required."))

        if cd.get('phone_number') is None:
            raise forms.ValidationError(_("Phone name is empty or invalid."))

        if cd.get('email_id') is None:
            raise forms.ValidationError(_("Email ID name is required."))

        return cd


class AuthyForm(forms.Form):
    """
    Authy Form
    """
    authy = forms.CharField(widget=forms.NumberInput, required=True,
                            help_text="Enter the number provided by the Authy application on your mobile.")
    is_personal = forms.BooleanField(required=False)

    def clean(self):

        cd = self.cleaned_data

        if not is_int(cd.get('authy')):
            raise forms.ValidationError('The string should be all numbers.')

        length = len(cd.get('authy'))
        if length < 6 or length > 12:
            raise forms.ValidationError('Unexpected length of input.')

        return cd


class LoginForm(AuthenticationForm):
    """
    Custom `AuthenticationForm` that forces staff to create a two-factor authentication.
    """
    remember_me = forms.BooleanField(required=False)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data
