from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'blog/$', views.post_list, name='post_list'),
    url(r'blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<date>\d{2})/(?P<post>[-\w]+)', views.post_detail,
        name='post_detail'),
]
