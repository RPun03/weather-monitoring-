from datetime import datetime
from sqlalchemy import func

# Example session setup
Session = sessionmaker(bind=engine)
session = Session()


def store_weather_data(data, city):
    # Convert temperature from Kelvin to Celsius
    temp_celsius = data["main"]["temp"]
    feels_like_celsius = data["main"]["feels_like"]
    weather_main = data["weather"][0]["main"]
    dt = datetime.utcfromtimestamp(data["dt"])

    weather_entry = WeatherData(
        city=city,
        main=weather_main,
        temp_celsius=temp_celsius,
        feels_like_celsius=feels_like_celsius,
        dt=dt,
    )

    session.add(weather_entry)
    session.commit()
