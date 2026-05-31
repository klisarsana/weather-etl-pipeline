import unittest

from src.extract.weather_extractor import WeatherExtractor
from src.transform.weather_transformer import WeatherTransformer
from src.load.weather_loader import WeatherLoader
from src.utils.db import get_db_conn, close_db_conn


class TestWeatherETLPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Initialize ETL components once
        """
        cls.extractor = WeatherExtractor()
        cls.transformer = WeatherTransformer()
        cls.loader = WeatherLoader()

    def test_1_extraction(self):
        """
        Test weather data extraction
        """
        raw_data = self.extractor.fetch_weather()

        self.assertIsNotNone(raw_data)
        self.assertIsInstance(raw_data, dict)

        self.__class__.raw_data = raw_data

    def test_2_transformation(self):
        """
        Test weather data transformation
        """
        transformed_data = self.transformer.transform(self.raw_data)

        self.assertIsNotNone(transformed_data)
        self.assertIsInstance(transformed_data, dict)

        required_fields = [
            "latitude",
            "longitude",
            "location_name",
            "country",
            "temperature",
            "feels_like",
            "humidity",
            "pressure",
            "weather_main",
            "weather_description",
            "wind_speed",
            "visibility",
            "recorded_at"
        ]

        for field in required_fields:
            self.assertIn(field, transformed_data)

        self.__class__.transformed_data = transformed_data

    def test_3_loading(self):
        """
        Test loading transformed data into database
        """
        self.loader.load(self.transformed_data)

        conn = get_db_conn()
        self.assertIsNotNone(conn)

        cursor = conn.cursor()

        query = """
            SELECT location_name, temperature
            FROM weather_data
            ORDER BY id DESC
            LIMIT 1
        """

        cursor.execute(query)
        result = cursor.fetchone()

        self.assertIsNotNone(result)

        cursor.close()
        close_db_conn(conn)


if __name__ == "__main__":
    unittest.main(verbosity=2)