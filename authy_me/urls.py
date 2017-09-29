from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete

from . import views

urlpatterns = [
    url(r'login/$', views.log_me_in, name='login'),
    url(r'login/2fa/$', views.auth_2fa, name='2fa_auth'),
    url(r'logout', views.log_me_out, name='logout'),
    url(r'portal/user/$', views.user, name='user_home'),
    url(r'portal/user/reset/$', password_reset, {'template_name': 'portal/user/auth/password_reset.html'},
        name='password_reset'),
    url(r'portal/user/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'portal/user/auth/password_reset_confirm.html',
         'post_reset_redirect': '/portal/user/reset_done/'},
        name='password_reset_confirm'),
    url(r'portal/user/reset/done/$', password_reset_done,
        {'template_name': 'portal/user/auth/password_reset_done.html'}, name='password_reset_done'),
    url(r'portal/user/reset_done/$', password_reset_complete, name='password_reset_complete'),
    url(r'portal/user/profile$', views.profile_home, name='profile_home'),
    url(r'portal/user/2fa/(?P<options>\w+)?$', views.two_fa_home, name='2fa_home'),
    url(r'portal/user/2fa/delete/$', views.delete_auth, name='delete_2fa'),
    url(r'portal/user/2fa/register/$', views.two_fa_register, name='2fa_register'),
    url(r'portal/user/2fa/register/confirm$', views.confirm_mobile, name='confirm_mobile'),
    url(r'^static/js/users\.js', views.users_js, name='users_js'),
]
