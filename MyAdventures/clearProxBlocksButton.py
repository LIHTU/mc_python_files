import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import anyio.seg7 as display
import RPi.GPIO as GPIO

clearButton = 23
LED_PINS = [10,22,25,8,7,9,11,15] #ORDER IMPORTANT

GPIO.setmode(GPIO.BCM)
GPIO.setup(clearButton, GPIO.IN)

ON = False
display.setup(GPIO, LED_PINS, ON)

mc = minecraft.Minecraft.create()

# finish function
def clearNear(x, y, z):
    radius = 1
    mc.setBlocks(x-radius, y-radius, z-radius, x+radius, y+radius+1, z+radius, block.AIR.id)

try:
    while True:
        time.sleep(0.1)
        if GPIO.input(clearButton) == False:
            pos = mc.player.getTilePos()
            clearNear(pos.x, pos.y, pos.z)
            

            

finally:
    GPIO.cleanup()

