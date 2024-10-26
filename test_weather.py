import unittest
from unittest.mock import patch
from weather_data_collector import fetch_weather_data


class TestWeatherDataCollector(unittest.TestCase):

    @patch("weather_data_collector.requests.get")
    def test_fetch_weather_data_success(self, mock_get):
        # Mock the response from the OpenWeatherMap API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "main": {"temp": 295.15, "feels_like": 298.15},
            "weather": [{"main": "Clear"}],
            "dt": 1635245078,
        }

        city = "Delhi"
        data = fetch_weather_data(city)

        self.assertIsNotNone(data)
        self.assertEqual(data["main"]["temp"], 295.15)
        self.assertEqual(data["weather"][0]["main"], "Clear")

    @patch("weather_data_collector.requests.get")
    def test_fetch_weather_data_failure(self, mock_get):
        # Mock the response for a failed API call
        mock_get.return_value.status_code = 404

        city = "InvalidCity"
        data = fetch_weather_data(city)

        self.assertIsNone(data)


if __name__ == "__main__":
    unittest.main()
