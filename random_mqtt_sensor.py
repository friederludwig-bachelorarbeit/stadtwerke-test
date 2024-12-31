import random
from time import sleep
from datetime import datetime, timedelta, timezone
from mqtt_publisher import send_message
from utils import load_json

MOCK_DATA = "test-data/mock_sensor.json"
MQTT_BROKER = "localhost"
MQTT_PORT = 1883


def generate_random_payload(data):
    location = random.choice(data["locations"])
    status_type = random.choice(data["status_types"])
    machine_type = random.choice(data["machine_types"])
    machine_id = str(random.randint(1012, 1016))
    sensor_id = str(random.randint(205, 206))
    value = str(random.randint(10, 200))

    # Zufälliger Zeitstempel (innerhalb der letzten Stunde)
    timestamp = (datetime.now(timezone.utc) -
                 timedelta(minutes=random.randint(0, 60))).replace(microsecond=0).isoformat()

    return {
        "topic": f"stadtwerke/{location}/{machine_type}/{machine_id}/{status_type}/{sensor_id}",
        "payload": {
            "timestamp": timestamp,
            "value": value,
        }
    }


if __name__ == "__main__":
    mock_data = load_json(MOCK_DATA)
    num_messages = int(input("Anzahl der Nachrichten: "))

    for _ in range(num_messages):
        random_message = generate_random_payload(mock_data)

        send_message(
            MQTT_BROKER, MQTT_PORT, random_message["topic"], random_message["payload"])

        # sleep(1)
