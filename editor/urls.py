#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'portal/$', views.portal_home, name='portal_home'),
    url(r'portal/editor$', views.editor_home, name='editor_home'),
    url(r'portal/editor/content$', views.content_home, name='content_home'),
    url(r'portal/editor/education', views.education_content, name='education_home'),
    url(r'portal/editor/project', views.content_home, name='project_home'),
    url(r'portal/editor/tutorial', views.content_home, name='tutorial_home'),
    url(r'portal/editor/experience', views.content_home, name='experience_home'),
    url(r'portal/editor/skills', views.content_home, name='skills_home'),
    url(r'portal/editor/publication', views.content_home, name='publication_home'),
    url(r'portal/editor/meta', views.meta_home, name='meta_home'),
]
