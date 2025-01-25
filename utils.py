import json
import random
from datetime import datetime, timedelta, timezone


def load_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(f"❌ Datei nicht gefunden: {file_path}")
        raise e
    except json.JSONDecodeError as e:
        print(f"❌ Ungültiges JSON in der Datei: {file_path}")
        raise e


def generate_current_timestamp():
    now = datetime.now(timezone.utc)
    # Format für Millisekunden hinzufügen
    return now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
