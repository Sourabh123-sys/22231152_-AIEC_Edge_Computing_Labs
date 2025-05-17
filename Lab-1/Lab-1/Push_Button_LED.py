import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)   # LED on GPIO4
GPIO.setup(17, GPIO.IN)    # Button on GPIO17

try:
    while True:
        if GPIO.input(17):  
            GPIO.output(4, True)
        else:
            GPIO.output(4, False)
except KeyboardInterrupt:
    GPIO.cleanup()
