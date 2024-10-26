CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    main VARCHAR(50),
    temp_celsius FLOAT,
    feels_like_celsius FLOAT,
    dt TIMESTAMP,
    recorded_at TIMESTAMP DEFAULT NOW()
);

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
