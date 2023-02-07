from django.urls import path

from user_auth.views import *

app_name = 'user_auth'

urlpatterns = [
    path('success/', success, name='success'),

    path('', to_login_redirect, name='user-login'),

    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('remind/', UserRemindView.as_view(), name='user-remind'),

    path('remind/<str:code>/', UserResetPasswordView.as_view(), name='user-remind'),
]
