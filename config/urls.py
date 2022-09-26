from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user.urls")),
    path('', include("product.urls")),
    path('', include("weather.urls")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redocs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
