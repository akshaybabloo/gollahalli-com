from django.db import models


class WelcomeToAbies(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=120, default='1', unique=True)
    firs_name = models.CharField(max_length=120, name='welcome_first_name')
    last_name = models.CharField(max_length=120, name='welcome_last_name')
    email_id = models.EmailField(name='welcome_email_id')
    company_name = models.CharField(max_length=240, name='welcome_company_name')
    title_same_as_company = models.BooleanField(name='welcome_title_same_as_company')
    AWS_SECRET = models.CharField(max_length=120, name='welcome_AWS_SECRET')
    AWS_SECRET_KEY = models.CharField(max_length=120, name='welcome_AWS_SECRET_KEY')
    AWS_S3_BUCKET_NAME = models.CharField(max_length=120, name='welcome_AWS_S3_BUCKET_NAME')
    root_username = models.CharField(max_length=120, name='welcome_root_username')
    root_password = models.CharField(max_length=30, name='welcome_root_password')
