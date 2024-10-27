import time
from weather.data_fetch import fetch_weather_data, store_weather_data
from weather.data_aggregator import rollup_daily_summaries
from weather.alerting import check_alert_thresholds
from config import OPENWEATHER_API_KEY

# List of cities to monitor
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Monitoring interval (in seconds) – Set it to 300 seconds for every 5 minutes
FETCH_INTERVAL = 300


def main():
    print("Starting Weather Monitoring System...")

    while True:
        print("Fetching weather data...")
        for city in CITIES:
            # Fetch weather data for each city
            weather_data = fetch_weather_data(city, OPENWEATHER_API_KEY)

            if weather_data:
                # Store the fetched weather data into the database
                store_weather_data(weather_data, city)

                # Check if any alert conditions are met
                check_alert_thresholds(weather_data, city)

        print("Weather data fetched and stored. Sleeping for next interval...")

        # Roll up daily summaries at the end of each day or at a scheduled time (can be implemented)
        rollup_daily_summaries()

        # Wait for the configured interval (e.g., 5 minutes)
        time.sleep(FETCH_INTERVAL)


if __name__ == "__main__":
    main()
