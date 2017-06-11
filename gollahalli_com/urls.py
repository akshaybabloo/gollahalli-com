"""
Main URL settings page. See https://docs.djangoproject.com/en/1.10/topics/http/urls/ for more information.
"""
import datetime
import json
import os

import requests
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.sitemaps import views
from django.http import HttpResponse
from graphene_django.views import GraphQLView

from .schema import *
from .sitemaps import *

GITHUB_KEY = os.environ['GITHUB_KEY']


def get_version():
    """
    Get's the latest released version.

    Returns
    -------
    response: dict:
        A dictionary of GitHub content.

    """
    response = requests.get('https://api.github.com/repos/akshaybabloo/gollahalli-me/releases/latest',
                            auth=('akshaybabloo', GITHUB_KEY))
    return json.loads(response.text)


def github_date_time_format(value):
    """
    Strips the date and time of GitHub's format.

    Parameters
    ----------
    value: str
        The vale should be of format `%Y-%m-%dT%H:%M:%Sz`.

    Returns
    -------
    date: datetime
        datetime object.
    """
    date = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%Sz')
    return date


def custom_date(value):
    """
    Strips users date.

    >>> c_date = custom_date('10/10/2010')

    Parameters
    ----------
    value: str
        The vale should be of format `%d/%m/%Y`.

    Returns
    -------
    date: datetime
        datetime object
    """
    date = datetime.datetime.strptime(value, '%d/%m/%Y')
    return date


sitemaps = {
    'pages': Sitemap(
        ['index'],
        [1.0],
        ['monthly'],
        [datetime.date.today()]
    ),

    'other': Sitemap(
        ['repo', 'change-log'],
        [0.5, 1.0],
        ['monthly', 'monthly'],
        [custom_date('10/01/2017'), github_date_time_format(get_version()['published_at'])]
    )
}

urlpatterns = [
                  url(r'^', include('viewer.urls')),
                  url(r'^editor/', include('editor.urls'), name='editor_urls'),
                  url(r'^admin/', admin.site.urls, name='admin_urls'),
                  url(r'^accounts/login/$', login, {'template_name': 'login.html'}, name="login"),
                  url(r'^accounts/logout/$', logout),
                  # url(r'^accounts/password/reset/$', password_reset, {'template_name': 'userauth/password_change_form.html'}, name="password_reset"),
                  # url(r'^accounts/password/password-change-done/$', password_change_done, {'template_name': 'userauth/password_change_done.html'}, name="password_change_done"),
                  url(r'^accounts/profile/', include('editor.urls'), name="profile"),
                  url(r'^robots.txt',
                      lambda x: HttpResponse(
                          "Sitemap: https://www.gollahalli.com/sitemap.xml\nUser-agent: *\nDisallow: /admin/\nDisallow: /cdn-cgi/",
                          content_type="text/plain"), name="robots_file"),
                  url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps, 'template_name': 'sitemap-index.xml'}),
                  url(r'^sitemap-(?P<section>.+).xml$', views.sitemap,
                      {'sitemaps': sitemaps, 'template_name': 'sitemap.xml'},
                      name='django.contrib.sitemaps.views.sitemap'),
                  url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=query)),
                  url(r'^filer/', include('filer.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'viewer.views.page_not_found'
handler500 = 'viewer.views.server_error'
