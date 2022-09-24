from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]