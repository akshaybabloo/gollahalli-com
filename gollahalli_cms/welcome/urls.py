from django.conf.urls import url

from gollahalli_cms.welcome import views

urlpatterns = [
    url(r'welcome/$', views.home, name='welcome'),
    url(r'welcome/check/db/$', views.check_db_conn, name='check_db'),
    url(r'welcome/check/aws/$', views.check_aws, name='check_aws'),
    url(r'welcome/check/ssl/$', views.check_ssl, name='check_ssl'),
    url(r'welcome/check/s3/$', views.check_aws_s3, name='check_s3'),
    url(r'welcome/check/smtp/$', views.check_smtp, name='check_smtp'),
    url(r'welcome/check/authy/$', views.check_authy, name='check_smtp'),
]
