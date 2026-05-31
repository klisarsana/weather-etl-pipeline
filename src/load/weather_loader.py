from src.utils.db import get_db_conn, close_db_conn
from src.utils.logger import logger

class WeatherLoader:
    def load(self, transformed_data):
        """
        Load transformed weather data into PostgreSQL
        """
        conn = None
        cursor = None

        try:
            conn = get_db_conn()

            if conn is None:
                logger.error('Failed to connect to database')
                return
            cursor = conn.cursor()

            insert_query = """
                INSERT INTO weather_data (
                    latitude,
                    longitude,
                    location_name,
                    country,
                    temperature,
                    feels_like,
                    humidity,
                    pressure,
                    weather_main,
                    weather_description,
                    wind_speed,
                    visibility,
                    recorded_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                transformed_data['latitude'],
                transformed_data['longitude'],
                transformed_data['location_name'],
                transformed_data['country'],
                transformed_data['temperature'],
                transformed_data['feels_like'],
                transformed_data['humidity'],
                transformed_data['pressure'],
                transformed_data['weather_main'],
                transformed_data['weather_description'],
                transformed_data['wind_speed'],
                transformed_data['visibility'],
                transformed_data['recorded_at']
            )

            cursor.execute(insert_query, values)
            conn.commit()

            logger.info('Weather data loaded successfully')

        except Exception as e:
            logger.error(f'Loading failed: {e}')

        finally:
            if cursor:
                cursor.close()
            if conn:
                close_db_conn(conn)