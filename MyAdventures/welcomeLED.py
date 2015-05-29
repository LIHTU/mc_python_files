import time
#import RPi.GPIO as GPIO
import anyio.GPIO as GPIO
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

LED = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

HOME_X = 244
HOME_Y = 121
HOME_Z = 470

mc.setBlock(HOME_X, HOME_Y, HOME_Z, block.WOOL.id, 15)

def flash(t):
    GPIO.output(LED, True)
    time.sleep(t)
    GPIO.output(LED, False)
    time.sleep(t)

try:
    while True:
        pos = mc.player.getTilePos()
        if pos.x == HOME_X and pos.z == HOME_Z:
            flash(0.5)
finally:
    GPIO.cleanup()
