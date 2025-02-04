import random
from time import sleep
from mqtt_publisher import send_message
from utils import load_json, generate_current_timestamp

MOCK_DATA = "test-data/mock_sensor.json"
MQTT_BROKER = "localhost"
MQTT_PORT = 1883

SLEEP_SECONDS_PER_INTERVAL = 0.1


def generate_random_payload(data):
    location = random.choice(data["locations"])
    status_type = random.choice(data["meassurement"])
    machine_type = random.choice(data["machine_types"])
    machine_id = str(random.randint(1012, 1016))
    sensor_id = str(random.randint(205, 206))

    # Zufälliger Zeitstempel (innerhalb der letzten Stunde)
    timestamp = generate_current_timestamp()

    # Wert basierend auf dem Meassurement-Typ
    if status_type == "error":
        value = random.choice(data["error_messages"])
    elif status_type == "temperature":
        value = str(random.randint(28, 90))
    elif status_type == "pressure":
        value = str(random.randint(50, 150))
    else:
        value = "unknown"

    # Message Objekt für den MQTT Broker
    return {
        "topic": f"stadtwerke/{location}/{machine_type}/{machine_id}/{status_type}/{sensor_id}",
        "payload": {
            "timestamp": timestamp,
            "value": value,
        }
    }


if __name__ == "__main__":
    mock_data = load_json(MOCK_DATA)

    print("Starting the endless random message sender loop...")
    try:
        while True:
            random_message = generate_random_payload(mock_data)

            send_message(
                MQTT_BROKER,
                MQTT_PORT,
                random_message["topic"],
                random_message["payload"])

            print(
                f"Sent message. Waiting for {SLEEP_SECONDS_PER_INTERVAL} second(s)...")

            sleep(SLEEP_SECONDS_PER_INTERVAL)

    except KeyboardInterrupt:
        print("\nStopping the message sender loop.")
