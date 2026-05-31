import json
from datetime import datetime

from config.settings import PROCESSED_DATA_DIR
from src.utils.logger import logger

class WeatherTransformer:
    def transform(self, raw_data):
        """
        Transform raw weather API data into structured format.
        """

        try:
            transformed_data = {
                "latitude": raw_data["coord"]["lat"],
                "longitude": raw_data["coord"]["lon"],
                "location_name": raw_data["name"],
                "country": raw_data["sys"]["country"],
                "temperature": raw_data["main"]["temp"],
                "feels_like": raw_data["main"]["feels_like"],
                "humidity": raw_data["main"]["humidity"],
                "pressure": raw_data["main"]["pressure"],
                "weather_main": raw_data["weather"][0]["main"],
                "weather_description": raw_data["weather"][0]["description"],
                "wind_speed": raw_data["wind"]["speed"],
                "visibility": raw_data["visibility"],
                "recorded_at": datetime.now().isoformat()
            }

            self._save_processed_data(transformed_data)

            logger.info('Weather data transformed successfully')
            return transformed_data

        except Exception as e:
            logger.error(f'Transformation failed: {e}')
            return None

    def _save_processed_data(self, data):
        """
        Save transformed data to processed folder
        """

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = PROCESSED_DATA_DIR / f'processed_{timestamp}.json'

        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

            logger.info(f'Processed data saved to: {file_path}')

        except Exception as e:
            logger.error(f'Failed to save processed data: {e}')