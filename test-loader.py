from src.extract.weather_extractor import WeatherExtractor
from src.transform.weather_transformer import WeatherTransformer
from src.load.weather_loader import WeatherLoader


extractor = WeatherExtractor()
transformer = WeatherTransformer()
loader = WeatherLoader()

raw_data = extractor.fetch_weather()

if raw_data:
    transformed_data = transformer.transform(raw_data)

    if transformed_data:
        loader.load(transformed_data)
        print("ETL pipeline completed successfully")