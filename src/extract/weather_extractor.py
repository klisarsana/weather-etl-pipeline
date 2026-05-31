import json
import requests
from datetime import datetime

from config.settings import (
    API_KEY,
    BASE_URL,
    LAT,
    LON,
    RAW_DATA_DIR,
    REQUEST_TIMEOUT,
)

from src.utils.logger import logger

class WeatherExtractor:
    def __init__(self):
        self.lat = LAT
        self.lon = LON
        self.api_key = API_KEY

    def fetch_weather(self):
        """
        Fetch realtime weather data using latitude and longitude.
        """
        params = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": self.api_key,
            "units": "metric",
        }

        try:
            logger.info(
                f'Starting extraction for coordinates: ({self.lat}, {self.lon})'
            )

            response = requests.get(
                BASE_URL,
                params=params,
                timeout=REQUEST_TIMEOUT,
            )

            response.raise_for_status()
            data = response.json()
            logger.info('Weather data extracted successfully')
            self._save_raw_data(data)

            return data

        except requests.exceptions.RequestException as e:
            logger.error(f'Extraction failed: {e}')
            return None

    def _save_raw_data(self, data):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        file_path = RAW_DATA_DIR / f'weather_{timestamp}.json'

        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

            logger.info(f'Raw data saved to {file_path}')
        except Exception as e:
            logger.error(f'Failed to save raw data: {e}')