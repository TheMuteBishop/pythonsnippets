from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth

from . import views
app_name = 'users'

urlpatterns = [
    path('register', views.register, name='user-register'),
    path('profile', views.profile, name='user-profile'),
    path('login', auth.LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout', auth.LogoutView.as_view(template_name='users/logout.html') , name='user-logout'),
    path('password-reset/',
         auth.PasswordResetView.as_view(
             template_name='users/reset.html',success_url = reverse_lazy('users:password_reset_done')
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth.PasswordResetDoneView.as_view(
             template_name='users/reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth.PasswordResetConfirmView.as_view(
             template_name='users/reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth.PasswordResetCompleteView.as_view(
             template_name='users/reset_complete.html'
         ),
         name='password_reset_complete'),
]
