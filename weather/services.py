from core.services import BaseModelService
from .models import WeatherType


class WeatherService(BaseModelService):
    model_class = WeatherType

    def create(self, request, validated_data, **kwargs):
        pass

    def update(self, request, instance, validated_data, **kwargs):
        pass

    def update_status(self, request, instance, validated_data):
        pass
