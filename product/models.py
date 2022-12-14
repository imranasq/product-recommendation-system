from core.models import BaseModel
from django.db import models
from user.models import User

from weather.models import WeatherType


class ProductType(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Product(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/product/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    product_type = models.ForeignKey(ProductType, related_name='product_category',
                                     on_delete=models.SET_NULL, null=True, blank=True)
    weather_type = models.ForeignKey(WeatherType, related_name='products_weather',
                                     on_delete=models.SET_NULL, null=True, blank=True)
    vendor = models.ForeignKey(User, related_name='product_vendor', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

