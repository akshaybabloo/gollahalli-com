from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps import views
from django.contrib.auth.views import login, logout
from django.http import HttpResponse

from .sitemaps import *

sitemaps = {
    'pages': Sitemap(['index', 'repo', 'change-log']),
}

urlpatterns = [
    url(r'^', include('viewer.urls')),
    url(r'^editor/', include('editor.urls'), name='editor_urls'),
    url(r'^admin/', admin.site.urls, name='admin_urls'),
    url(r'^accounts/login/$', login, {'template_name': 'admin/login.html'}, name="my_login"),
    url(r'^accounts/logout/$', logout),
    url(r'^robots.txt',
        lambda x: HttpResponse("Sitemap: https://www.gollahalli.me/sitemap.xml\nUser-agent: *\nDisallow: /admin/",
                               content_type="text/plain"), name="robots_file"),
    url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^sitemap-(?P<section>.+).xml$', views.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = 'viewer.views.page_not_found'
handler500 = 'viewer.views.server_error'
