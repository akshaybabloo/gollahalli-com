#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

from django.urls import path

from viewer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('repo/', views.get_github_repo, name='repo'),
    path('change-log/', views.get_gollahalli_me_change_log, name='change-log'),
    path('cookie-policy/', views.get_cookie_policy, name='cookie-policy')
]
