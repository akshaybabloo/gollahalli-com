"""
Main URL settings page. See https://docs.djangoproject.com/en/1.10/topics/http/urls/ for more information.
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps import views
from django.contrib.auth.views import login, logout, password_reset, password_change_done
from django.http import HttpResponse
from graphene_django.views import GraphQLView

from .sitemaps import *
from .schema import *

sitemaps = {
    'pages': Sitemap(['index'], 1.0),
    'other': Sitemap(['repo', 'change-log'], 0.5)
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
        lambda x: HttpResponse("Sitemap: https://www.gollahalli.com/sitemap.xml\nUser-agent: *\nDisallow: /admin/",
                               content_type="text/plain"), name="robots_file"),
    url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps, 'template_name': 'sitemap-index.xml'}),
    url(r'^sitemap-(?P<section>.+).xml$', views.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=query)),
]

handler404 = 'viewer.views.page_not_found'
handler500 = 'viewer.views.server_error'
