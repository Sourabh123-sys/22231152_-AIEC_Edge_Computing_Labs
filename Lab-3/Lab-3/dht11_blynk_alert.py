# Lab_3_Blynk_IoT/dht11_blynk_alert.py
import Adafruit_DHT
from BlynkLib import Blynk

BLYNK_AUTH = "_t3bU6MIWbPE7gCifMI87D-aBvlN5wwq"  # From Blynk app
dht_sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO4

blynk = Blynk(BLYNK_AUTH)

def read_dht():
    hum, temp = Adafruit_DHT.read_retry(dht_sensor, pin)
    return hum, temp

while True:
    hum, temp = read_dht()
    if hum > 70:  # Alert if humidity > 70%
        blynk.notify("High Humidity Alert!")
    blynk.virtual_write(0, temp)  # Send to Blynk Virtual Pin 0
    blynk.virtual_write(1, hum)   # Send to Blynk Virtual Pin 1
    time.sleep(2)
