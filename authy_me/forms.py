from django import forms

from .models import AuthenticatorModel


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
