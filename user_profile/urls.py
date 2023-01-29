from django.urls import path

from user_profile.views import *

urlpatterns = [
    path('my/', index, name='my-profile'),
]
