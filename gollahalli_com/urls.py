"""
Main URL settings page. See https://docs.djangoproject.com/en/1.10/topics/http/urls/ for more information.
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps import views
from django.http import HttpResponse
from graphene_django.views import GraphQLView

from gollahalli_com.schema import query
from gollahalli_com.sitemaps import Sitemap, xsl_content_type, index_view
from gollahalli_com.utils import *

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

admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = [
                  url(r'^', include('viewer.urls')),
                  url(r'^', include('editor.urls'), name='editor_urls'),
                  url(r'^admin/', admin.site.urls, name='admin_urls'),
                  url(r'^', include('authy_me.urls'), name="login"),
                  url(r'^', include('welcome.urls')),
                  url(r'^', include('blog.urls')),
                  url(r'^robots.txt',
                      lambda x: HttpResponse(
                          "Sitemap: https://www.gollahalli.com/sitemap.xml\nUser-agent: *\nDisallow: "
                          "/admin/\nDisallow: /cdn-cgi/\nDisallow: /portal/",
                          content_type="text/plain"), name="robots_file"),
                  url(r'^sitemap\.xml$', index_view, {'sitemaps': sitemaps, 'template_name': 'sitemap-index.xml'}),
                  url(r'^sitemap-(?P<section>.+).xml$', views.sitemap,
                      {'sitemaps': sitemaps, 'template_name': 'sitemap.xml'},
                      name='django.contrib.sitemaps.views.sitemap'),
                  url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=query)),
                  url(r'^sitemap\.xsl', xsl_content_type, name='sitemap_xsl')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'viewer.views.page_not_found'
handler500 = 'viewer.views.server_error'
