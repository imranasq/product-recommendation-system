import pytest
from factory.django import DjangoModelFactory
import factory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = 'user.User'

    email = 'user@mail.com'
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall('set_password', 'admin@123')


class AdminUserFactory(DjangoModelFactory):
    class Meta:
        model = 'user.User'

    email = 'admin@mail.com'
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall('set_password', 'admin@123')
    user_type = "Admin"
    is_admin = True
    is_superuser = True
    is_staff = True
    is_active = True

