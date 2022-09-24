from django.urls import path, include
from weather.views import (
    WeatherAPIViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'weather', WeatherAPIViewSet, basename='weather')

urlpatterns = [
    path("", include(router.urls)),
]
