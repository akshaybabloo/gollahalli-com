from django import forms
from django.contrib.auth.models import (User, Group)

from .models import AuthenticatorModel


class AuthenticatorAdminForm(forms.ModelForm):
    """
    AuthenticatorModel form for admin view.
    """

    user_id = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={"onChange": 'refresh()'}))

    class Meta:
        model = AuthenticatorModel
        fields = '__all__'

    class Media:
        js = ('users.js',)

