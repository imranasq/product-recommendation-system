import pytest

from product.serializers import (
    ProductSerializer,
    ProductTypeSerializer,
    ProductStatusUpdateSerializer,
    ProductTypeStatusUpdateSerializer
)

pytestmark = pytest.mark.django_db


class TestProductTypeSerializer:
    Serializer = ProductTypeSerializer

    def test_valid_serializer(self):
        """Test that correct data is validated"""
        data = {
            "name": "string"
        }
        serializer = self.Serializer(data=data)
        assert serializer.is_valid()
        assert dict(serializer.validated_data) == data

    def test_invalid_serializer(self):
        """Test that invalid data is not validated"""
        data = {
            "name": True
        }
        serializer = self.Serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert "name" in serializer.errors
        assert (serializer.errors["name"][
                    0].lower() == 'not a valid string.')


class TestProductSerializer:
    Serializer = ProductSerializer

    @pytest.mark.parametrize(
        "data",
        [
            {
                "title": 'string',
            },
            {
                "title": 'title',
                "price": 1234,
            },
            {
                "title": 'title',
                "price": 1234,
                "quantity": 50
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
            "price": 500,
        }
        serializer = self.Serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert "title" in serializer.errors
        assert (serializer.errors["title"][
                    0].lower() == 'this field is required.')


class TestProductTypeStatusUpdateSerializer:
    Serializer = ProductTypeStatusUpdateSerializer

    def test_valid_serializer(self):
        payload = {
            "is_active": True,
        }
        """Test that correct data is validated"""
        serializer = self.Serializer(data=payload)
        assert serializer.is_valid()
        assert dict(serializer.validated_data) == payload

    def test_invalid_serializer(self):
        data = {"is_active": 1234}
        serializer = self.Serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert "is_active" in serializer.errors
        assert serializer.errors["is_active"][0].code == "invalid"
        assert (
                serializer.errors["is_active"][0].lower()
                == "must be a valid boolean.")


class TestProductStatusUpdateSerializer:
    Serializer = ProductStatusUpdateSerializer

    def test_valid_serializer(self):
        payload = {
            "is_active": True,
        }
        """Test that correct data is validated"""
        serializer = self.Serializer(data=payload)
        assert serializer.is_valid()
        assert dict(serializer.validated_data) == payload

    def test_invalid_serializer(self):
        data = {"is_active": 1234}
        serializer = self.Serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert "is_active" in serializer.errors
        assert serializer.errors["is_active"][0].code == "invalid"
        assert (
                serializer.errors["is_active"][0].lower()
                == "must be a valid boolean.")
