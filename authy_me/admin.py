from django.contrib import admin

from .models import AuthenticatorModel
from .forms import AuthenticatorAdminForm


class AuthenticatorAdmin(admin.ModelAdmin):
    """
    AuthenticatorModel admin.
    """
    list_display = ['user_id']
    form = AuthenticatorAdminForm

admin.site.register(AuthenticatorModel, AuthenticatorAdmin)
