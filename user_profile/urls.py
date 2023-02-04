from django.urls import path

from user_auth.views import success
from user_profile.views import *

app_name = 'user_profile'

urlpatterns = [
    path('success/', success, name='success'),

    path('main-info/', FillMainInfoProfile.as_view(), name='my-profile'),
    path('contact/', FillContactProfile.as_view(), name='my-contact'),
    path('my/remove/', remove_m_profile, name='remove-my-profile'),

]
