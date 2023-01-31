from django.urls import path

from user_profile.views import *

app_name = 'vacancy'

urlpatterns = [
    path('vacancy-list/', index, name='vacancy-list'),
]
