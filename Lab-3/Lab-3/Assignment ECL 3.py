import Adafruit_DHT
import RPi.GPIO as GPIO
from BlynkLib import Blynk
import time

# DHT11 Sensor Setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  

# Blynk IoT Setup
BLYNK_AUTH_TOKEN = "_t3Bu6MIWbPE7DCifMI87D-aBvIN5wwq"  

HUMIDITY_THRESHOLD = 70  # Alert if humidity > 70%

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

def send_blynk_notification(message):
    blynk.log_event("high_humidity", message)
    print(f"ALERT: {message}")

try:
    while True:
        humidity, temperature = read_sensor()
        
        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature:.1f}°C | Humidity: {humidity:.1f}%")
            
            # Send data to Blynk
            blynk.virtual_write(0, temperature)  # Virtual Pin V0 (Temp)
            blynk.virtual_write(1, humidity)     # Virtual Pin V1 (Humidity)
            
            if humidity > HUMIDITY_THRESHOLD:
                alert_msg = f"High Humidity Detected: {humidity}%"
                send_blynk_notification(alert_msg)
        
        else:
            print("Failed to read sensor data!")
        
        time.sleep(2)  # Read every 2 seconds
        blynk.run()

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()