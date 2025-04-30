# Lab_1_GPIO_LED/LED_Blink_BCM
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)  # GPIO4 (Pin 7)

try:
    while True:
        GPIO.output(4, True)  # LED ON
        print("LED ON")
        time.sleep(1)
        GPIO.output(4, False)  # LED OFF
        print("LED OFF")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
