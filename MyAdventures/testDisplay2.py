import anyio.seg7 as display
#import RPi.GPIO as GPIO        pi

import anyio.GPIO as GPIO
import time

LED_PINS = [7,6,14,16,10,8,9,15]  # arduino
#LED_PINS = [10,22,25,8,7,9,11,15] # pi

GPIO.setmode(GPIO.BCM)

ON = False

display.setup(GPIO, LED_PINS, ON)

try:
    while True:
        for d in range(10):
            display.write(str(d))
            time.sleep(0.25)
        # robin's addition: display letters in letters list
        letters = ['A', 'b', 'C', 'd', 'E']
        for l in letters:
            display.write(l)
            time.sleep(.8)
finally:
    GPIO.cleanup()

