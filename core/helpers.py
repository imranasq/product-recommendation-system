import requests
from rest_framework import status
from config import settings
from core.exceptions import CustomException


def get_temperature_from_weather_api(lat, lon):
    temperature_data = {}
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.WEATHER_API_KEY}")
        temperature_data["temp"] = response.json()['main']['temp'] - 273.15  # Kalvin unit to Degree Celsius
    except Exception:
        raise CustomException(detail="Please provide Weather API key carefully!", status_code=status.HTTP_401_UNAUTHORIZED)
    return temperature_data
