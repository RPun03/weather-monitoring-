import requests
from config import OPENWEATHER_API_KEY
from models import WeatherData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time


def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def store_weather_data(data):
    # Convert and store in database
    pass
