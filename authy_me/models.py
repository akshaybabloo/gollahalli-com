import phonenumbers
from authy.api import AuthyApiClient
from django.conf import settings
from django.contrib.auth.models import (User, Group)
from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class AuthenticatorModel(models.Model):
    """
    `AuthenticatorModel` creates a two-factor authentication using `Authy`.
    """

    def __init__(self, *args, **kwargs):
        self.status = {}
        super().__init__(*args, **kwargs)

    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    user_id = models.ForeignKey(User, related_name='auth_user', null=True)
    first_name = models.CharField(default='First Name', max_length=50)
    last_name = models.CharField(default='Last Name', max_length=50)
    phone_number = PhoneNumberField()
    email_id = models.CharField(default='email ID', help_text='Enter the email ID used to register the Django user',
                                max_length=50)
    authy_id = models.CharField(null=True,
                                max_length=50)
    session_id = models.CharField(null=True, max_length=100)

    def create_authy(self):
        """
        Creates a Authy user account and returns an unique ID

        Returns
        -------
        user: object
            object by Authy.
        """
        phone_number = phonenumbers.parse(str(self.phone_number))

        authy_api = AuthyApiClient(settings.AUTHY_API)

        user = authy_api.users.create(self.email_id, phone_number.national_number, phone_number.country_code)

        if user.ok():
            return user.id
        else:
            self.status = user.errors()
            return 'error'

    def delete_authy(self):
        """
        Deletes Authy user.

        Returns
        -------
        user: object
            object of Authy.
        """
        authy_api = AuthyApiClient(settings.AUTHY_API)

        user = authy_api.users.delete(self.authy_id)

        if user.errors():
            self.status = user.errors()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Saves `AuthenticatorModel` model and updates the `User` model.

        Parameters
        ----------
        force_insert
        force_update
        using
        update_fields

        Returns
        -------
        object
        """

        try:
            obj = User.objects.get(id=self.id)
        except User.DoesNotExist:
            return

        obj.first_name = self.first_name
        obj.last_name = self.last_name
        obj.email = self.email_id
        obj.save()

        self.authy_id = self.create_authy()

        return super(AuthenticatorModel, self).save()

    def clean(self):

        if self.authy_id == 'error':
            raise ValidationError({
                'authy_id': _(self.status)
            })

    def delete(self, using=None, keep_parents=False):
        """
        Deletes Authy user and the model content.

        Parameters
        ----------
        using
        keep_parents

        Returns
        -------
        super
        """

        self.delete_authy()

        return super(AuthenticatorModel, self).delete()
