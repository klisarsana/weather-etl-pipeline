import logging

from config.settings import LOG_FILE


def setup_logger():
    """
    Membuat dan mengatur logger untuk ETL Pipeline.
    """

    logger = logging.getLogger("weather_etl")
    # Hindari duplicate handler
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    # file handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# inisialisasi logger
logger = setup_logger()
