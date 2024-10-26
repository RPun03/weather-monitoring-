from sqlalchemy import Column, Integer, String, Float, Date, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), nullable=False)
    main = Column(String(50), nullable=False)
    temp_celsius = Column(Float, nullable=False)
    feels_like_celsius = Column(Float, nullable=False)
    dt = Column(DateTime, nullable=False)
    recorded_at = Column(DateTime, default=func.now())


class DailySummary(Base):
    __tablename__ = "daily_summary"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    avg_temp = Column(Float, nullable=False)
    max_temp = Column(Float, nullable=False)
    min_temp = Column(Float, nullable=False)
    dominant_condition = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())
