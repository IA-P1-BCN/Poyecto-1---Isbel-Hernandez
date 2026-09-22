import json
from pathlib import Path

HISTORY_PATH = Path("data/history.jsonl")


def save_trip(trip_data):
    with HISTORY_PATH.open("a") as file:
        file.write(json.dumps(trip_data) + "\n")

def load_history():
    if not HISTORY_PATH.exists():
        return []

    with HISTORY_PATH.open() as file:
        return [json.loads(line) for line in file if line.strip()]
    