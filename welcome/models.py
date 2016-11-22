from django.db import models


class WelcomeToAbies(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=120, default='1', unique=True)
    firs_name = models.CharField(max_length=120, default='null', name='welcome_first_name')
    last_name = models.CharField(max_length=120, default='null', name='welcome_last_name')
    email_id = models.EmailField(name='welcome_email_id')
    profile_image_location = models.CharField(max_length=240, default='null', name='welcome_profile_image_location')
    company_logo_location = models.CharField(max_length=240, default='null', name='welcome_company_logo_location')
    company_name = models.CharField(max_length=240, default='null', name='welcome_company_name')
    # AWS_SECRET = models.CharField(max_length=120, default='null', name='welcome_AWS_SECRET')
    # AWS_SECRET_KEY = models.CharField(max_length=120, default='null', name='welcome_AWS_SECRET_KEY')
    # AWS_S3_BUCKET_NAME = models.CharField(max_length=120, default='null', name='welcome_AWS_S3_BUCKET_NAME')
    root_username = models.CharField(max_length=120, default='null', name='welcome_root_username')
    root_password = models.CharField(max_length=30, default='null', name='welcome_root_password')
