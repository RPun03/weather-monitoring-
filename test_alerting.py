import unittest
from weather.alerting import check_alert_thresholds


class TestAlerting(unittest.TestCase):

    def setUp(self):
        # Sample weather data for testing
        self.sample_data_below_threshold = {"main": {"temp": 293.15}}  # 20°C in Kelvin
        self.sample_data_above_threshold = {"main": {"temp": 310.15}}  # 37°C in Kelvin
        self.city = "Delhi"

    def test_no_alert_below_threshold(self):
        """
        Test that no alert is triggered when temperature is below threshold.
        """
        # Capture print output
        with self.assertLogs("weather.alerting", level="INFO") as cm:
            check_alert_thresholds(self.sample_data_below_threshold, self.city)
            self.assertNotIn("ALERT", str(cm.output))

    def test_alert_triggered_above_threshold(self):
        """
        Test that an alert is triggered when temperature exceeds threshold.
        """
        # Capture print output
        with self.assertLogs("weather.alerting", level="INFO") as cm:
            check_alert_thresholds(self.sample_data_above_threshold, self.city)
            self.assertIn("ALERT: Temperature in Delhi exceeds 35°C.", str(cm.output))


if __name__ == "__main__":
    unittest.main()
