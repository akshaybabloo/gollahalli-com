#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli
"""
Production file for Heroku.
"""

import os

import dj_database_url
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config(conn_max_age=500)
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

SHARE_URL = "https://www.gollahalli.com/"

# S3
AWS_S3_CALLING_FORMAT = 'boto.s3.connection.OrdinaryCallingFormat'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'cdn.gollahalli.com'
AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = 'cdn.gollahalli.com'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storage.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storage.MediaStorage'
