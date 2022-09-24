from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category
from .services import ProductService, CategoryService

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    service_class = ProductService
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    service_class = CategoryService
    permission_classes = [IsAuthenticated]