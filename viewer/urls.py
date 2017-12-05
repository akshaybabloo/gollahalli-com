#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'repo/', views.get_github_repo, name='repo'),
    url(r'change-log/', views.get_gollahalli_me_change_log, name='change-log'),
    url(r'cookie-policy/', views.get_cookie_policy, name='cookie-policy')
]
