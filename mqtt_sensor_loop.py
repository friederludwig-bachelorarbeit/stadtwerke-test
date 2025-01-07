import random
from time import sleep
from mqtt_publisher import send_message
from utils import load_json, generate_random_timestamp

MOCK_DATA = "test-data/mock_sensor.json"
MQTT_BROKER = "localhost"
MQTT_PORT = 1883

SLEEP_SECONDS_PER_INTERVAL = 1
MIN_MESSAGES_PER_INTERVAL = 10
MAX_MESSAGES_PER_INTERVAL = 25


def generate_random_payload(data):
    location = random.choice(data["locations"])
    status_type = random.choice(data["status_types"])
    machine_type = random.choice(data["machine_types"])
    machine_id = str(random.randint(1012, 1016))
    sensor_id = str(random.randint(205, 206))
    value = str(random.randint(10, 200))

    # Zufälliger Zeitstempel (innerhalb der letzten Stunde)
    timestamp = generate_random_timestamp()

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
            # Zufällige Anzahl von Messages
            num_messages = random.randint(
                MIN_MESSAGES_PER_INTERVAL,
                MAX_MESSAGES_PER_INTERVAL)

            for _ in range(num_messages):
                random_message = generate_random_payload(mock_data)

                send_message(
                    MQTT_BROKER,
                    MQTT_PORT,
                    random_message["topic"],
                    random_message["payload"])

            print(
                f"Sent {num_messages} messages. Waiting for {SLEEP_SECONDS_PER_INTERVAL} second(s)...")

            sleep(SLEEP_SECONDS_PER_INTERVAL)

    except KeyboardInterrupt:
        print("\nStopping the message sender loop.")
