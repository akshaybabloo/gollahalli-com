#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

from django.conf.urls import url

from editor import views

urlpatterns = [
    url(r'portal/$', views.portal_home, name='portal_home'),
    url(r'portal/editor$', views.editor_home, name='editor_home'),
    url(r'portal/editor/content$', views.content_home, name='content_home'),
    url(r'portal/editor/content/edit$', views.content_home, name='content_home_edit'),
    url(r'portal/editor/education', views.education_content, name='education_home'),
    url(r'portal/editor/education/edit', views.education_content, name='education_home_edit'),
    url(r'portal/editor/project', views.projects_content, name='project_home'),
    url(r'portal/editor/project/edit', views.projects_content, name='project_home_edit'),
    url(r'portal/editor/tutorial', views.tutorials_content, name='tutorial_home'),
    url(r'portal/editor/tutorial/edit', views.tutorials_content, name='tutorial_home_edit'),
    url(r'portal/editor/experience', views.experience_content, name='experience_home'),
    url(r'portal/editor/experience/edit', views.experience_content, name='experience_home_edit'),
    url(r'portal/editor/skills', views.skills_content, name='skills_home'),
    url(r'portal/editor/skills/edit', views.skills_content, name='skills_home_edit'),
    url(r'portal/editor/publication', views.publications_content, name='publication_home'),
    url(r'portal/editor/publication/edit', views.publications_content, name='publication_home_edit'),
    url(r'portal/editor/meta', views.meta_home, name='meta_home'),
    url(r'portal/editor/meta/edit', views.meta_home, name='meta_home_edit'),
]
