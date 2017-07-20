from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login/$', views.log_me_in, name='login'),
    url(r'login/2fa/$', views.auth_2fa, name='2fa_auth'),
    url(r'logout', views.log_me_out, name='logout'),
    url(r'portal/user/$', views.user, name='user_home'),
    url(r'portal/user/profile$', views.profile_home, name='profile_home'),
    url(r'portal/user/2fa/$', views.two_fa_home, name='2fa_home'),
    url(r'portal/user/2fa/delete/$', views.delete_auth, name='delete_2fa'),
    url(r'portal/user/2fa/register/$', views.two_fa_register, name='2fa_register'),
    url(r'portal/user/2fa/register/confirm$', views.confirm_mobile, name='confirm_mobile'),
    url(r'^static/js/users\.js', views.users_js, name='users_js'),
]
