import pytest
from rest_framework.reverse import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestWeatherViewSet:
    payload = {
        "weather": 'Normal',
        "minimum_temperature": 15,
        "maximum_temperature": 25
    }

    def test_get_weather_with_unauthentic_client(self, client):
        url = reverse("weather-list")
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() is not None

    def test_get_weather_with_authentic_client(self, auth_client):
        url = reverse("weather-list")
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None

    def test_create_weather_with_unauthentic_client(self, client):
        payload = self.payload
        url = reverse("weather-list")
        response = client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() is not None

    def test_create_weather_with_authentic_client(self, auth_client):
        payload = self.payload
        url = reverse("weather-list")
        response = auth_client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.json() is not None

    def test_create_weather_with_admin_client(self, admin_client):
        payload = self.payload
        url = reverse("weather-list")
        response = admin_client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() is not None

    def test_create_weather_with_no_payload(self, admin_client):
        url = reverse("weather-list")
        response = admin_client.post(url, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() is not None

    def test_update_weather_with_admin_client(self, admin_client, weather_type):
        payload = self.payload
        url = reverse("weather-detail", kwargs={"pk": weather_type.id})
        response = admin_client.put(url, data=payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None

    def test_partial_update_weather_with_admin_client(self, admin_client, weather_type):
        payload = {
            "minimum_temperature": 10
        }
        url = reverse("weather-detail", kwargs={"pk": weather_type.id})
        response = admin_client.patch(url, data=payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None

    def test_update_weather_with_auth_client(self, auth_client, weather_type):
        payload = self.payload
        url = reverse("weather-detail", kwargs={"pk": weather_type.id})
        response = auth_client.put(url, data=payload, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.json() is not None

    def test_partial_update_weather_with_auth_client(self, auth_client, weather_type):
        payload = {
            "minimum_temperature": 10
        }
        url = reverse("weather-detail", kwargs={"pk": weather_type.id})
        response = auth_client.patch(url, data=payload, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.json() is not None

    def test_delete_weather_with_admin_client(self, admin_client, weather_type):
        url = reverse("weather-detail", kwargs={"pk": weather_type.id})
        response = admin_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_weather_with_auth_client(self, auth_client, weather_type):
        url = reverse("weather-detail", kwargs={"pk": weather_type.id})
        response = auth_client.delete(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_weather_with_existing_data(self, admin_client, weather_type):
        payload = {
            "weather": weather_type.weather,
            "minimum_temperature": weather_type.minimum_temperature,
            "maximum_temperature": weather_type.maximum_temperature
        }
        url = reverse("weather-list")
        response = admin_client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() is not None
