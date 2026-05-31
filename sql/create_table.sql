CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT,
    location_name VARCHAR(100),
    country VARCHAR(10),
    temperature FLOAT,
    feels_like FLOAT,
    humidity INT,
    pressure INT,
    weather_main VARCHAR(50),
    weather_description VARCHAR(100),
    wind_speed FLOAT,
    visibility INT,
    recorded_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);