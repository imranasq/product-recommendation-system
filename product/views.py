from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.views import BaseModelViewSet

from .serializers import (
    ProductSerializer,
    ProductTypeSerializer,
    ProductDetailSerializer,
    ProductStatusUpdateSerializer,
    ProductTypeStatusUpdateSerializer
)
from .models import Product, ProductType
from .services import ProductService, ProductTypeService


class ProductViewSet(BaseModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    service_class = ProductService()
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
