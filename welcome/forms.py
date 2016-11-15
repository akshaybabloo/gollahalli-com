#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

from django import forms


class WelcomeForm(forms.Form):
    firs_name = forms.CharField(max_length=120, name='welcome_first_name')
    last_name = forms.CharField(max_length=120, name='welcome_last_name')
    email_id = forms.EmailField(name='welcome_email_id')
    company_name = forms.CharField(max_length=240, name='welcome_company_name')
    title_same_as_company = forms.CheckboxSelectMultiple()
    AWS_SECRET = forms.CharField(max_length=120, name='welcome_AWS_SECRET')
    AWS_SECRET_KEY = forms.CharField(widget=forms.PasswordInput)
    AWS_S3_BUCKET_NAME = forms.CharField(max_length=120, name='welcome_AWS_S3_BUCKET_NAME')
    root_username = forms.CharField(max_length=120, name='welcome_root_username')
    root_password = forms.CharField(widget=forms.PasswordInput)
