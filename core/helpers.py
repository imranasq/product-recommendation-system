import requests
from config import settings

def get_temperature(city):
    temperature_data = {}
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.WEATHER_API_KEY}")
        temperature_data["temp"] = response.json()['main']['temp']
        temperature_data["min_temp"] = response.json()["main"]["temp_min"]
        temperature_data["max_temp"] = response.json()["main"]["temp_max"]
    except Exception:
        raise Exception
    return temperature_data
