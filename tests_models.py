import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import WeatherData, DailySummary, Base


class TestDatabaseModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up an in-memory SQLite database for testing
        cls.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

    def test_weather_data_creation(self):
        weather = WeatherData(
            city="Delhi",
            main="Clear",
            temp_celsius=22.0,
            feels_like_celsius=23.0,
            dt="2024-01-01 12:00:00",
        )
        self.session.add(weather)
        self.session.commit()

        # Query back the inserted data
        retrieved = self.session.query(WeatherData).filter_by(city="Delhi").first()
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.temp_celsius, 22.0)

    def test_daily_summary_creation(self):
        summary = DailySummary(
            city="Delhi",
            date="2024-01-01",
            avg_temp=20.0,
            max_temp=25.0,
            min_temp=15.0,
            dominant_condition="Clear",
        )
        self.session.add(summary)
        self.session.commit()

        # Query back the inserted data
        retrieved = self.session.query(DailySummary).filter_by(city="Delhi").first()
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.avg_temp, 20.0)


if __name__ == "__main__":
    unittest.main()
