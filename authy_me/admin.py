from django.contrib import admin
from django import forms

from .models import AuthenticatorModel


class AuthenticatorForm(forms.ModelForm):
    """
    AuthenticatorModel form for admin view.
    """

    class Meta:
        model = AuthenticatorModel
        fields = '__all__'


class AuthenticatorAdmin(admin.ModelAdmin):
    """
    AuthenticatorModel admin.
    """
    list_display = ['user_id']
    form = AuthenticatorForm

admin.site.register(AuthenticatorModel, AuthenticatorAdmin)
