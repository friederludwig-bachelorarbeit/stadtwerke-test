import json
import paho.mqtt.client as mqtt


def send_message(broker: str, port: int, topic: str, payload: str):
    try:
        client = mqtt.Client()
        client.connect(broker, port)
        payload_str = json.dumps(payload)

        client.publish(topic, payload_str)

        print(f"✅ Nachricht an Topic '{topic}' gesendet: {payload_str}")

        client.disconnect()
    except Exception as e:
        print(f"❌ Fehler beim Senden der Nachricht: {e}")
