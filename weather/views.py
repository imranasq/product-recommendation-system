from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import WeatherTypeSerializer
from .services import WeatherTypeService
from .models import WeatherType


class WeatherAPIViewSet(viewsets.ModelViewSet):
    queryset = WeatherType.objects.all()
    serializer_class = WeatherTypeSerializer
    service_class = WeatherTypeService()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
