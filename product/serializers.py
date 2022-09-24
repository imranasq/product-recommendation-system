from rest_framework import serializers
from .models import Product, ProductType
from weather.serializers import WeatherConditionSerializer


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name', 'is_active']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price", "quantity", "category", "vendor", "is_active"]
        read_only_fields = ["is_active", "vendor"]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = ProductTypeSerializer(read_only=True)
    weather_condition = WeatherConditionSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "is_active"]
