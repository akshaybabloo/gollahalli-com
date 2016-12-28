from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth.views import login, logout

from .sitemaps import *

sitemaps = {
    'pages': Sitemap(['index']),
}

urlpatterns = [
    url(r'^', include('viewer.urls')),
    url(r'^editor/', include('editor.urls'), name='editor_urls'),
    url(r'^admin/', admin.site.urls, name='admin_urls'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^accounts/login/$', login, {'template_name': 'admin/login.html'}, name="my_login"),
    url(r'^accounts/logout/$', logout),
]

handler404 = 'viewer.views.page_not_found'
handler500 = 'viewer.views.server_error'
