import pytest
from config import settings
from product.tests.factories import ProductTypeFactory, ProductFactory
from user.tests.factories import UserFactory
from weather.tests.factories import WeatherTypeFactory
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass


@pytest.fixture()
def user():
    return UserFactory()


@pytest.fixture()
def product_type():
    return ProductTypeFactory()


@pytest.fixture()
def product():
    return ProductFactory()


@pytest.fixture()
def weather_type():
    return WeatherTypeFactory()


@pytest.fixture
def client():
    client = APIClient()
    return client


def create_user():
    return UserFactory.create()


@pytest.fixture
def auth_client(client):
    user = create_user()
    client.force_authenticate(user)
    return client


@pytest.fixture
def unauthorized_client():
    unauthorized_client = APIClient()
    return unauthorized_client
