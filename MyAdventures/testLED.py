import time
#import RPi.GPIO as GPIO
import anyio.GPIO as GPIO

LED = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def flash(t):
    GPIO.output(LED, True)
    time.sleep(t)
    GPIO.output(LED, False)
    time.sleep(t)

try:
    while True:
        flash(0.5)
finally:
    GPIO.cleanup()
