# Testsystem für IoT-Datenerfassungssystem für Stadtwerke

Dieses Projekt dient dazu, das IoT-Datenerfassungssystem für die Stadtwerke zu testen. Es sendet in einem festgelegten Intervall zufällig generierte Nachrichten aus den Daten in `test-data/` an das System. Dabei werden sowohl normale Statusmeldungen und Informationen als auch Fehlermeldungen erzeugt.

##  Installation & Einrichtung

### Virtuelle Umgebung erstellen
Damit alle Abhängigkeiten sauber installiert werden, sollte eine virtuelle Umgebung (venv) genutzt werden.

```bash
# Erstelle eine virtuelle Umgebung
python -m venv venv  

# Aktiviere die virtuelle Umgebung 
# Auf Windows:
venv\Scripts\activate  

# Auf macOS/Linux:
source venv/bin/activate  

# Installiere die Abhängigkeiten 
pip install -r requirements.txt
```

## Nachrichten-Loop starten

Um den Loop zur Erzeugung von MQTT-Nachrichten zu starten, führe folgenden Befehl aus:

```bash
python mqtt_sensor_loop.py
```

In `mqtt_sensor_loop.py` kann auch die Anzahl der Nachrichten pro Sekunde über `SLEEP_SECONDS_PER_INTERVAL` festgelegt werden.
