# clears blocks surrounding player for specified radius with button

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
# import RPi.GPIO as GPIO
import anyio.GPIO as GPIO

clearButton = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(clearButton, GPIO.IN)

ON = False

mc = minecraft.Minecraft.create()

# clears blocks around player.  Great for mining or getting through walls.
def clearNear(x, y, z):
    radius = 20
    mc.setBlocks(x-radius, y-radius, z-radius, x+radius, y+radius+1, z+radius, block.AIR.id)

try:
    while True:
        time.sleep(0.1)
        if GPIO.input(clearButton) == False:
            pos = mc.player.getTilePos()
            clearNear(pos.x, pos.y, pos.z)

finally:
    GPIO.cleanup()
