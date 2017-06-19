from django.db import models
from django.contrib.auth.models import (User, Group)
from phonenumber_field.modelfields import PhoneNumberField


class AuthenticatorModel(models.Model):
    user_id = models.ForeignKey(User, related_name='auth_user', null=True)
    first_name = models.CharField(default='First Name', max_length=50)
    last_name = models.CharField(default='Last Name', max_length=50)
    phone_number = PhoneNumberField()
    email_id = models.CharField(default='email ID', help_text='Enter the email ID used to register the Django user', max_length=50)
