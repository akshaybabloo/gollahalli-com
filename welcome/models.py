from django.db import models


class AbiesModel(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=120, default='1', unique=True)

    # page 1
    first_name = models.CharField(max_length=120, name='first_name', blank=True)
    last_name = models.CharField(max_length=120, name='last_name', blank=True)
    email = models.EmailField(name='email', blank=True)
    profile_image_location = models.ImageField(upload_to='images', name='profile_image_location', blank=True)

    # page 2
    # AWS_SECRET = models.CharField(max_length=120, default='null', name='welcome_AWS_SECRET')
    # AWS_SECRET_KEY = models.CharField(max_length=120, default='null', name='welcome_AWS_SECRET_KEY')
    # AWS_S3_BUCKET_NAME = models.CharField(max_length=120, default='null', name='welcome_AWS_S3_BUCKET_NAME')
    username = models.CharField(max_length=120, name='username', blank=True)
    password = models.CharField(max_length=30, name='password', blank=True)

    # page 3
    company_logo_location = models.ImageField(upload_to='images', name='company_logo_location', blank=True)
    company_name = models.CharField(max_length=240, name='company_name', blank=True)
    city = models.CharField(max_length=240, name='city', blank=True)
    country = models.CharField(max_length=240, name='country', blank=True)
