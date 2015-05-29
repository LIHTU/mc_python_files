import time
import RPi.GPIO as GPIO
LED_PINS = [10,22,25,8,7,9,11,15] #ORDER IMPORTANT

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

def show_numbers():
    # 0
    pattern = [True, True, True, True, True, True, False, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)
    
    # 1
    pattern = [False, True, True, False, False, False, False, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)

    # 2
    pattern = [True, True, False, True, True, False, True, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)

    # 3
    pattern = [True, True, True, True, False, False, True, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)

    # 4
    pattern = [False, True, True, False, False, True, True, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)

    # 5
    pattern = [True, False, True, True, False, True, True, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)

    # 6
    pattern = [True, False, True, True, True, True, True, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)

    # 7
    pattern = [True, True, True, False, False, False, False, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)

    # 8
    pattern = [True, True, True, True, True, True, True, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)

    # 9
    pattern = [True, True, True, False, False, True, True, False]
    for g in range(8):
        if pattern[g]:
            GPIO.output(LED_PINS[g], ON)
        else:
            GPIO.output(LED_PINS[g], not ON)
    time.sleep(.3)

show_numbers()

raw_input("finished?")

GPIO.cleanup()
