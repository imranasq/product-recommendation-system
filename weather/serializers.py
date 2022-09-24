from weather.models import WeatherCondition
from rest_framework import serializers


class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCondition
        fields = ['id', 'weather', 'minimum_temperature', 'maximum_temperature']
