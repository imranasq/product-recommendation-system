from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import WeatherConditionSerializer
from .services import WeatherService
from .models import WeatherCondition


class WeatherAPIViewSet(viewsets.ModelViewSet):
    queryset = WeatherCondition.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = WeatherConditionSerializer
    service_class = WeatherService
    http_method_names = ['get', 'post', 'put']
