import logging

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import AuthenticatorModel

logger = logging.getLogger(__name__)


class AuthenticatorAdminForm(forms.ModelForm):
    """
    AuthenticatorModel form for admin view.
    """

    authy_id = forms.CharField(widget=forms.NumberInput, disabled=True, required=False)

    class Meta:
        model = AuthenticatorModel
        fields = '__all__'

    class Media:
        js = ('//code.jquery.com/jquery-3.2.1.min.js',
              'js/users.js',)


class OTPForm(forms.Form):
    pass


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
