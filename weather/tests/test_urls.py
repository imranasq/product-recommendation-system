import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_weather_list_url():
    assert reverse("weather-list") == "/weather/"
    assert resolve("/weather/").view_name == "weather-list"


def test_weather_detail_url(weather_type):
    assert reverse("weather-detail", kwargs={"pk": weather_type.id}) == f"/weather/{weather_type.id}/"
    assert resolve(f"/weather/{weather_type.id}/").view_name == "weather-detail"
