from src.extract.weather_extractor import WeatherExtractor
from src.transform.weather_transformer import WeatherTransformer
from src.load.weather_loader import WeatherLoader
from src.utils.logger import logger

def run_pipeline():
    try:
        logger.info('Starting ETL Pipeline...')

        extractor = WeatherExtractor()
        transformer = WeatherTransformer()
        loader = WeatherLoader()

        # Extract
        raw_data = extractor.fetch_weather()
        if not raw_data:
            logger.error('Extraction failed')
            return
            
        # Transform
        transformed_data = transformer.transform(raw_data)
        if not transformed_data:
            logger.error('Transformation failed')
            return
        
        # Load
        loader.load(transformed_data)
        logger.info('ETL Pipeline completed successfully')

    except Exception as e:
        logger.error(f'Pipeline failed: {e}')

if __name__ == '__main__':
    run_pipeline()