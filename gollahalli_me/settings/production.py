#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

import os

import dj_database_url
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

TEMPLATE_DEBUG = False

DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
DATABASES['default'] = dj_database_url.config()
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

SHARE_URL = "http://www.gollahalli.me/"

# S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAIPQQUJGYXMFFOASA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'gollahalli-me-django'
AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = 'gollahalli-heroku-django-ypyxfkub.stackpathdns.com'


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
