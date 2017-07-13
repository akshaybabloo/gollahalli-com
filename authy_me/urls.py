from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login/$', views.log_me_in, name='login'),
    url(r'login/2fa/', views.auth_2fa, name='2fa'),
    url(r'user/', views.user, name='user'),
    url(r'user/security/', views.security, name='security'),
    url(r'user/security/2fa/register', views.auth_2fa_register, name='2fa_register'),
    url(r'^static/js/users\.js', views.users_js, name='users_js'),
]
