from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
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
    user_id = models.ForeignKey(User, related_name='auth_user', null=True, on_delete=None)
    first_name = models.CharField(default='First Name', max_length=50)
    last_name = models.CharField(default='Last Name', max_length=50)
    phone_number = PhoneNumberField()
    email_id = models.EmailField(default='test@test.com',
                                 help_text='Enter the email ID used to register the Django user',
                                 max_length=50)
    authy_id = models.CharField(null=True,
                                max_length=50)
    session_id = models.CharField(null=True, max_length=100)
    uuids = JSONField(default={})

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
            obj = User.objects.get(username=self.user_id)
        except User.DoesNotExist:
            return

        obj.first_name = self.first_name
        obj.last_name = self.last_name
        obj.email = self.email_id
        obj.save()

        return super(AuthenticatorModel, self).save()
