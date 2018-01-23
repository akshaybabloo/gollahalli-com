#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

from django.urls import path

from editor import views

urlpatterns = [
    path('portal/', views.portal_home, name='portal_home'),
    path('portal/editor', views.editor_home, name='editor_home'),
    path('portal/editor/content', views.content_home, name='content_home'),
    path('portal/editor/content/edit', views.content_home, name='content_home_edit'),
    path('portal/editor/education', views.education_content, name='education_home'),
    path('portal/editor/education/edit', views.education_content, name='education_home_edit'),
    path('portal/editor/project', views.projects_content, name='project_home'),
    path('portal/editor/project/edit', views.projects_content, name='project_home_edit'),
    path('portal/editor/tutorial', views.tutorials_content, name='tutorial_home'),
    path('portal/editor/tutorial/edit', views.tutorials_content, name='tutorial_home_edit'),
    path('portal/editor/experience', views.experience_content, name='experience_home'),
    path('portal/editor/experience/edit', views.experience_content, name='experience_home_edit'),
    path('portal/editor/skills', views.skills_content, name='skills_home'),
    path('portal/editor/skills/edit', views.skills_content, name='skills_home_edit'),
    path('portal/editor/publication', views.publications_content, name='publication_home'),
    path('portal/editor/publication/edit', views.publications_content, name='publication_home_edit'),
    path('portal/editor/meta', views.meta_home, name='meta_home'),
    path('portal/editor/meta/edit', views.meta_home, name='meta_home_edit'),
]
