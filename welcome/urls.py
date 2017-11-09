from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'welcome/$', views.home, name='portal_home'),
]
