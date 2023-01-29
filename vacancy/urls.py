from django.urls import path

from user_profile.views import *

urlpatterns = [
    path('vacancy-list/', index, name='vacancy-list'),
]
