from itertools import product
from core.services import BaseModelService
from product.models import Product, Category


class ProductService(BaseModelService):
    model_class = Product


class CategoryService(BaseModelService):
    model_class = Category