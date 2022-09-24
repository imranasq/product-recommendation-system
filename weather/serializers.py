from weather.models import WeatherType
from rest_framework import serializers


class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherType
        fields = ['id', 'weather', 'minimum_temperature', 'maximum_temperature']
