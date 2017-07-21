#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'portal/$', views.portal_home, name='portal_home'),
    url(r'portal/editor$', views.editor_home, name='editor_home'),
    # url(r'^login/', views.login, name='index_login'),  # for custom login's
]
