import logging

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import AuthenticatorModel
from .utils import is_int

logger = logging.getLogger(__name__)


class AuthenticatorAdminForm(forms.ModelForm):
    """
    AuthenticatorModel form for admin view.
    """

    authy_id = forms.CharField(widget=forms.NumberInput, disabled=True, required=False,
                               help_text='This ID is provided by Authy and cannot be changed.')
    session_id = forms.CharField(disabled=True, required=False, help_text='This field is auto generated.')

    class Meta:
        model = AuthenticatorModel
        fields = '__all__'

    class Media:
        js = ('//code.jquery.com/jquery-3.2.1.min.js',
              'js/users.js',)


class AuthyForm(forms.Form):
    """
    Authy Form
    """
    authy = forms.CharField(required=True,
                            help_text="Enter the number provided by the Authy application on your mobile.")

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

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data
