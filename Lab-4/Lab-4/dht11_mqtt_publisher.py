# Lab_4_MQTT_Broker/dht11_mqtt_publisher.py
import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
import json

# Sensor Configuration
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4      # GPIO4 

# MQTT Configuration
MQTT_BROKER = "localhost"  
MQTT_PORT = 1883
MQTT_TOPIC = "home/sensor/dht11"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with code: {rc}")

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

# Initialize MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

try:
    while True:
        humidity, temperature = read_sensor()
        
        if humidity is not None and temperature is not None:
            
            payload = json.dumps({
                "temperature": temperature,
                "humidity": humidity,
                "unit": "C"
            })
            
            # Publish to MQTT
            client.publish(MQTT_TOPIC, payload)
            print(f"Published: {payload}")
        else:
            print("Failed to read sensor data")
        
        time.sleep(5)  

except KeyboardInterrupt:
    client.loop_stop()
    print("Script terminated")
