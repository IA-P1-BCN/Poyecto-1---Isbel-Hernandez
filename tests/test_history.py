import json

from src.infrastructure.history import load_history, save_trip
from datetime import datetime


def test_save_trip(tmp_path, monkeypatch):
    history_file = tmp_path / "history.jsonl"

    monkeypatch.setattr(
        "src.infrastructure.history.HISTORY_PATH",
        history_file
    )

    trip_data = {
        "date": "2026-09-22T14:30:00",
        "duration": 120,
        "amount": "1.40"
    }

    save_trip(trip_data)

    content = history_file.read_text()
    saved_trip = json.loads(content)

    assert saved_trip == trip_data


def test_load_history(tmp_path, monkeypatch):
    history_file = tmp_path / "history.jsonl"

    monkeypatch.setattr(
        "src.infrastructure.history.HISTORY_PATH",
        history_file
    )

    trip_data = {
        "date": datetime.now().replace(
    hour=14, minute=30, second=0, microsecond=0
        ).isoformat(),
        "duration": 120,
        "amount": "1.40"
    }

    save_trip(trip_data)

    history = load_history()

    assert history == [trip_data]