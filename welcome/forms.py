#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

from django import forms
from .models import WelcomeToAbies


class WelcomeForm(forms.Form):
    # page 1
    first_name = forms.CharField(max_length=120, required=False)
    last_name = forms.CharField(max_length=120, required=False)
    profile_image_location = forms.FileField(required=False)
    email = forms.EmailField(required=False)

    # page 2
    username = forms.CharField(max_length=120, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)
    # AWS_SECRET = forms.CharField(max_length=120)
    # AWS_SECRET_KEY = forms.CharField(widget=forms.PasswordInput)
    # AWS_S3_BUCKET_NAME = forms.CharField(max_length=120)

    # page 3
    company_name = forms.CharField(max_length=240, required=False)
    company_logo_location = forms.FileField(required=False)
    city = forms.CharField(max_length=120, required=False)
    country = forms.CharField(max_length=120, required=False)


# class WelcomeFormModel(forms.ModelForm):
#     class Meta:
#         model = WelcomeToAbies
#         fields = ('welcome_first_name', 'welcome_last_name')
