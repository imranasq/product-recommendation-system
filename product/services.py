from core.services import BaseModelService
from product.models import Product, ProductType


class ProductService(BaseModelService):
    model_class = Product


class ProductTypeService(BaseModelService):
    model_class = ProductType
