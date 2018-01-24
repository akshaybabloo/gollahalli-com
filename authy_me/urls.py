from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from authy_me import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('login/2fa/', views.auth_2fa, name='2fa_auth'),
    path('logout', views.log_me_out, name='logout'),
    path('portal/user/reset/',
         auth_views.PasswordResetView.as_view(template_name='portal/user/auth/password_reset.html'),
         name='password_reset'),
    path('portal/user/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='portal/user/auth/password_reset_confirm.html',
                                                     success_url='/portal/user/reset_done/'),
         name='password_reset_confirm'),
    path('portal/user/reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='portal/user/auth/password_reset_done.html'),
         name='password_reset_done'),
    path('portal/user/reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('portal/user/profile', views.profile_home, name='profile_home'),
    re_path(r'portal/user/2fa/(?P<options>\w+)?$', views.two_fa_home, name='2fa_home'),
    path('portal/user/2fa/delete/', views.delete_auth, name='delete_2fa'),
    path('portal/user/2fa/register/', views.two_fa_register, name='2fa_register'),
    path('portal/user/2fa/register/confirm', views.confirm_mobile, name='confirm_mobile'),
    path('static/js/users\.js', views.users_js, name='users_js'),
]
