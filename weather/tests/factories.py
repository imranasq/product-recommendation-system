import pytest
from factory.django import DjangoModelFactory
import factory


class WeatherTypeFactory(DjangoModelFactory):
    class Meta:
        model = 'weather.WeatherType'

    weather = "Normal"
    minimum_temperature = 15
    maximum_temperature = 25
