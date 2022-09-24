from django.db import models


class WeatherCondition(models.Model):
    WEATHER_CHOICES = (
        ('Hot', 'Hot'),
        ('Normal', 'Normal'),
        ('Cold', 'Cold')
    )
    weather = models.CharField(max_length=50, choices=WEATHER_CHOICES, unique=True)
    minimum_temperature = models.FloatField()
    maximum_temperature = models.FloatField()

    def __str__(self):
        return self.weather
