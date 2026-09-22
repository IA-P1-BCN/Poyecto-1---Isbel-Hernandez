import json
from decimal import Decimal
from pathlib import Path


CONFIG_PATH = Path("config/tariffs.json")


def load_tariffs():
    with CONFIG_PATH.open() as file:
        config = json.load(file)

    return {
        "stopped_rate": Decimal(config["stopped_rate"]),
        "moving_rate": Decimal(config["moving_rate"]),
    }