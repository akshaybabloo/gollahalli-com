from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.users_js, name='users_js'),
    url(r'login/$', views.log_me_in, name='login'),
    url(r'login/2fa/', views.auth_2fa, name='2fa'),
    url(r'^static/js/users\.js', views.users_js, name='authy_me_urls'),
]
