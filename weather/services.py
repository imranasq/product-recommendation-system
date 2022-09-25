from core.services import BaseModelService
from .models import WeatherType


class WeatherTypeService(BaseModelService):
    model_class = WeatherType
