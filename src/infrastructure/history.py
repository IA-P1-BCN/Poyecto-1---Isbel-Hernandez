import json
from pathlib import Path
from datetime import datetime

HISTORY_PATH = Path("data/history.jsonl")


def save_trip(trip_data):
    with HISTORY_PATH.open("a") as file:
        file.write(json.dumps(trip_data) + "\n")

def load_history():
    if not HISTORY_PATH.exists():
        return []

    today = datetime.now().date()

    with HISTORY_PATH.open() as file:
        history = [json.loads(line) for line in file if line.strip()]

    return [
        trip for trip in history
        if datetime.fromisoformat(trip["date"]).date() == today
    ]