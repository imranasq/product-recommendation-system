import pytest

from user.serializers import UserSerializer, ProfileSerializer, RegistrationSerializer

pytestmark = pytest.mark.django_db


class TestUserSerializer:
    Serializer = UserSerializer

    @pytest.mark.parametrize(
        "data",
        [
            {
                "email": 'test@mail.com',
            },
            {
                "email": 'test@mail.com',
                "user_type": "Admin",
            },
            {
                "email": 'test@mail.com',
                "user_type": "Admin",
                "first_name": "Random",
            },
            {
                "email": 'test@mail.com',
                "user_type": "Admin",
                "first_name": "Random",
                "last_name": "Name"
            },
        ],
    )
    def test_valid_serializer(self, data):
        """Test that correct data is validated"""
        serializer = self.Serializer(data=data)
        assert serializer.is_valid()
        assert dict(serializer.validated_data) == data

    def test_invalid_serializer(self):
        """Test that invalid data is not validated"""
        data = {
            "email": "something"
        }
        serializer = self.Serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert "email" in serializer.errors
        assert (serializer.errors["email"][
                    0].lower() == 'enter a valid email address.')


class TestProfileSerializer:
    Serializer = ProfileSerializer

    def test_valid_serializer(self, user):
        data = {
            "user": user.id,
            "bio": "something"
        }
        serializer = self.Serializer(data=data)
        assert serializer.is_valid()

    def test_invalid_serializer(self):
        """Test that invalid data is not validated"""
        data = {
            "user": "something"
        }
        serializer = self.Serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert "user" in serializer.errors
        assert (serializer.errors["user"][
                    0].lower() == 'incorrect type. expected pk value, received str.')


class TestUserRegistrationSerializer:
    Serializer = RegistrationSerializer

    def test_valid_serializer(self):
        """Test that correct data is validated"""
        data = {
            "email": 'test@mail.com',
            "user_type": "Admin",
            "password": "admin@123",
            "password2": "admin@123"
        }
        serializer = self.Serializer(data=data)
        assert serializer.is_valid()
        assert dict(serializer.validated_data) == data

    def test_invalid_serializer(self):
        """Test that invalid data is not validated"""
        data = {
            "email": "something",
            "user_type": "Admin",
            "password": "admin@123",
            "password2": "admin@123"
        }
        serializer = self.Serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert "email" in serializer.errors
        assert (serializer.errors["email"][
                    0].lower() == 'enter a valid email address.')
