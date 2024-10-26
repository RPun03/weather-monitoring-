Weather Monitoring System
Overview
This project is a real-time data processing system for monitoring weather conditions and generating summarized insights such as daily temperature averages, maximum and minimum temperatures, and dominant weather conditions. Data is retrieved continuously from the OpenWeatherMap API for specified cities in India, and the system supports user-configurable alert thresholds for temperature conditions.

Features
Real-Time Weather Data Collection:

Continuously fetches weather data from the OpenWeatherMap API at configurable intervals.
Stores each update in the weather_data table, including current temperature, weather conditions, and timestamps.
Daily Rollups and Summaries:

Aggregates daily weather data for each city.
Computes daily averages, maximum, and minimum temperatures and determines the dominant weather condition.
Stores these summaries in the daily_summary table.
User Alerts:

Allows user-configurable thresholds for temperature or specific weather conditions.
Triggers alerts if thresholds are breached (e.g., temperature exceeding 35°C for two consecutive updates).
Temperature Conversion:

Automatically converts temperature values from Kelvin (provided by the API) to Celsius.

System Design
1. Database Schema
The project uses a relational database (e.g., PostgreSQL or MySQL) to store both real-time weather data and daily summaries.

Schema Structure:
weather_data: Stores individual weather data records.
daily_summary: Stores aggregated daily weather summaries.
-- weather_data table
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    main VARCHAR(50),
    temp_celsius FLOAT,
    feels_like_celsius FLOAT,
    dt TIMESTAMP,
    recorded_at TIMESTAMP DEFAULT NOW()
);

-- daily_summary table
CREATE TABLE daily_summary (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    date DATE,
    avg_temp FLOAT,
    max_temp FLOAT,
    min_temp FLOAT,
    dominant_condition VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);

2. API Integration
The system retrieves weather data from the OpenWeatherMap API. You need to sign up for a free API key and configure it in the project.

Weather Parameters Fetched:
main: Main weather condition (e.g., Rain, Snow, Clear).
temp: Current temperature.
feels_like: Perceived temperature.
dt: Time of data update (Unix timestamp).

How It Works
Weather Data Collection:

weather_data_collector.py continuously calls the OpenWeatherMap API to fetch real-time weather data.
Converts temperatures from Kelvin to Celsius and stores the results in the weather_data table.
Daily Aggregation:

The system aggregates daily weather data and computes the following:
Average Temperature: The average temperature for the day.
Maximum Temperature: The highest recorded temperature for the day.
Minimum Temperature: The lowest recorded temperature for the day.
Dominant Condition: The most frequent weather condition for the day.
Stores this summary in the daily_summary table.

Threshold Alerting:

User-configurable thresholds (e.g., temperature exceeding 35°C) are compared with real-time data.
Triggers alerts when thresholds are breached (alerts can be printed to the console or sent via email).

Requirements
Python (3.7+)
PostgreSQL or MySQL
Requests (for API calls)
SQLAlchemy (for ORM)
Flask (optional, if building a web API)
