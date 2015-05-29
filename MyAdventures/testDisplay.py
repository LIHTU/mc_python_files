#import RPi.GPIO as GPIO
import anyio.GPIO as GPIO
#LED_PINS = [10,22,25,8,7,9,11,15] #Pi
LED_PINS = [7,6,14,16,10,8,9,15]

GPIO.setmode(GPIO.BCM)

ON = False # False = common-anode

for g in LED_PINS:
    GPIO.setup(g, GPIO.OUT)

pattern = [True, True, True, True, True, True, True, False] #ABCDEFG (no decimal point)

for g in range(8):
    if pattern[g]:
        GPIO.output(LED_PINS[g], ON)
    else:
        GPIO.output(LED_PINS[g], not ON)

raw_input("finished?")

GPIO.cleanup()
