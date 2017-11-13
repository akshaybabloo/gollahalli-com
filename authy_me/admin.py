from django.contrib import admin

from authy_me.models import AuthenticatorModel
from authy_me.forms import AuthenticatorAdminForm


class AuthenticatorAdmin(admin.ModelAdmin):
    """
    AuthenticatorModel admin.
    """
    list_display = ['id', 'user_id', 'phone_number', 'authy_id']
    form = AuthenticatorAdminForm


admin.site.register(AuthenticatorModel, AuthenticatorAdmin)
