import pytest

from weather.serializers import WeatherTypeSerializer

pytestmark = pytest.mark.django_db


class TestWeatherTypeSerializer:
    Serializer = WeatherTypeSerializer

    def test_valid_serializer(self):
        """Test that correct data is validated"""
        data = {
            "weather": "Hot",
            "minimum_temperature": 25,
            "maximum_temperature": 35
        }
        serializer = self.Serializer(data=data)
        assert serializer.is_valid()
        assert dict(serializer.validated_data) == data

    def test_invalid_serializer(self):
        """Test that invalid data is not validated"""
        data = {
            "weather": "Random",
            "minimum_temperature": 25,
            "maximum_temperature": 35
        }
        serializer = self.Serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert "weather" in serializer.errors
        assert (serializer.errors["weather"][
                    0].lower() == '"random" is not a valid choice.')
