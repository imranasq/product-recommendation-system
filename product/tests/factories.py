import pytest
from factory.django import DjangoModelFactory
import factory
from user.tests.factories import UserFactory
from weather.tests.factories import WeatherTypeFactory


class ProductTypeFactory(DjangoModelFactory):
    class Meta:
        model = 'product.ProductType'

    name = factory.Faker("pystr")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = 'product.Product'

    title = factory.Faker("pystr")
    description = factory.Faker("pystr")
    price = factory.Faker("random_int")
    quantity = factory.Faker("random_int")
    product_type = factory.SubFactory(ProductTypeFactory)
    weather_type = factory.SubFactory(WeatherTypeFactory)
    vendor = factory.SubFactory(UserFactory)
