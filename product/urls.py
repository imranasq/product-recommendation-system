from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductTypeViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'product-types', ProductTypeViewSet, basename='product_types')

urlpatterns = [
    path("", include(router.urls)),
]