import logging
from pathlib import Path


LOG_PATH = Path("data/taximetro.log")


def setup_logger():
    logger = logging.getLogger("taximetro")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(LOG_PATH)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger