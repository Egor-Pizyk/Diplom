from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('user_profile.urls')),
    path('vacancy/', include('vacancy.urls')),
    path('', include('user_auth.urls')),
]
