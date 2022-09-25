from rest_framework import serializers
from .models import Product, ProductType
from weather.serializers import WeatherTypeSerializer
from user.serializers import UserSerializer

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name', 'is_active']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "quantity", "product_type", "weather_type", "vendor",
                  "is_active"]
        read_only_fields = ["is_active"]


class ProductDetailSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer(read_only=True)
    weather_type = WeatherTypeSerializer(read_only=True)
    vendor = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "is_active"]


class ProductTypeStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'is_active']
