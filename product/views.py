from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.views import BaseModelViewSet
from django.db.models import Q
from core.helpers import get_temperature_from_weather_api

from .serializers import (
    ProductSerializer,
    ProductTypeSerializer,
    ProductDetailSerializer,
    ProductStatusUpdateSerializer,
    ProductTypeStatusUpdateSerializer
)
from .models import Product, ProductType
from .services import ProductService, ProductTypeService
from .filters import ProductFilter


class ProductViewSet(BaseModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    service_class = ProductService()
    filterset_class = ProductFilter
    permission_classes = [IsAuthenticated]
    update_status_serializer_class = ProductStatusUpdateSerializer

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ProductDetailSerializer
        else:
            return ProductSerializer

    def create(self, request, *args, **kwargs):
        if self.request.user.user_type == "Vendor":
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            self.service_class.create(request, validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'details': 'You do not have permission!'}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        if self.request.user.user_type == "Vendor" or self.request.user.user_type == "Admin":
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            instance = self.get_object()
            self.service_class.update(request, instance, validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'details': 'You do not have permission!'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if self.request.user.user_type == "Vendor" or self.request.user.user_type == "Admin":
            self.service_class.delete()
            return Response({'details': 'Item Deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'details': 'You do not have permission!'}, status=status.HTTP_401_UNAUTHORIZED)


class ProductTypeViewSet(BaseModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    service_class = ProductTypeService()
    permission_classes = [IsAuthenticated]
    update_status_serializer_class = ProductTypeStatusUpdateSerializer

    def create(self, request, *args, **kwargs):
        if self.request.user.user_type == "Admin":
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            self.service_class.create(request, validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'details': 'You do not have permission!'}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        if self.request.user.user_type == "Admin":
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            instance = self.get_object()
            self.service_class.update(request, instance, validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'details': 'You do not have permission!'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if self.request.user.user_type == "Admin":
            self.service_class.delete()
            return Response({'details': 'Item Deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'details': 'You do not have permission!'}, status=status.HTTP_401_UNAUTHORIZED)


class CustomerProductsAPIView(ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    model_class = Product

    def get_queryset(self):
        """
         For Filter products based on Latitude and Longitude collect from customer.
        """
        if self.request.GET.get("lat", None) and self.request.GET.get("lon", None):
            lat = self.request.query_params['lat']
            lon = self.request.query_params['lon']
            temperature_data = get_temperature_from_weather_api(lat, lon)
            if temperature_data:
                query_instance = Q(weather_type__maximum_temperature__gte=temperature_data["temp"]) & Q(
                    weather_type__minimum_temperature__lte=temperature_data["temp"])
                return self.model_class.objects.filter(query_instance)
