from core.services import BaseModelService
from .models import WeatherCondition


class WeatherService(BaseModelService):
    model_class = WeatherCondition

    def create(self, request, validated_data, **kwargs):
        pass

    def update(self, request, instance, validated_data, **kwargs):
        pass

    def update_status(self, request, instance, validated_data):
        pass
