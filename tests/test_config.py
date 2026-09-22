from decimal import Decimal

from src.infrastructure.config import load_tariffs


def test_load_tariffs():
    tariffs = load_tariffs()

    assert tariffs["stopped_rate"] == Decimal("0.02")
    assert tariffs["moving_rate"] == Decimal("0.05")