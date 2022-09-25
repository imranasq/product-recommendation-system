import requests
from config import settings


def get_temperature_from_weather_api(lat, lon):
    temperature_data = {}
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.WEATHER_API_KEY}")
        temperature_data["temp"] = response.json()['main']['temp'] - 273.15  # Kalvin unit to Degree Celsius
        temperature_data["min_temp"] = response.json()["main"]["temp_min"] - 273.15  # Kalvin unit to Degree Celsius
        temperature_data["max_temp"] = response.json()["main"]["temp_max"] - 273.15  # Kalvin unit to Degree Celsius
    except Exception:
        raise Exception
    return temperature_data
