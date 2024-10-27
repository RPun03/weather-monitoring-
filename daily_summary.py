from sqlalchemy import func


def create_daily_summary(city, date):
    # Fetch the weather data for the city on the given date
    results = (
        session.query(WeatherData)
        .filter(WeatherData.city == city, func.date(WeatherData.dt) == date)
        .all()
    )

    if results:
        temps = [r.temp_celsius for r in results]
        conditions = [r.main for r in results]

        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        dominant_condition = max(
            set(conditions), key=conditions.count
        )  # Most frequent condition

        # Store the daily summary
        summary = DailySummary(
            city=city,
            date=date,
            avg_temp=avg_temp,
            max_temp=max_temp,
            min_temp=min_temp,
            dominant_condition=dominant_condition,
        )

        session.add(summary)
        session.commit()


def rollup_daily_summaries():
    # This function should be scheduled to run daily (e.g., at midnight)
    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
    today = datetime.now().date()

    for city in cities:
        create_daily_summary(city, today)
