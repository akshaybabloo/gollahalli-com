from django.db import models


class WelcomeToAbies(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=120, default='1', unique=True)

    # page 1
    firs_name = models.CharField(max_length=120, default='null', name='first_name')
    last_name = models.CharField(max_length=120, default='null', name='last_name')
    email = models.EmailField(name='welcome_email_id')
    profile_image_location = models.ImageField(upload_to='images', name='profile_image_location')

    # page 2
    # AWS_SECRET = models.CharField(max_length=120, default='null', name='welcome_AWS_SECRET')
    # AWS_SECRET_KEY = models.CharField(max_length=120, default='null', name='welcome_AWS_SECRET_KEY')
    # AWS_S3_BUCKET_NAME = models.CharField(max_length=120, default='null', name='welcome_AWS_S3_BUCKET_NAME')
    username = models.CharField(max_length=120, default='null', name='username')
    password = models.CharField(max_length=30, default='null', name='password')

    # page 3
    company_logo_location = models.ImageField(upload_to='images', name='company_logo_location')
    company_name = models.CharField(max_length=240, default='null', name='company_name')
    city = models.CharField(max_length=240, default='null', name='city')
    country = models.CharField(max_length=240, default='null', name='country')
