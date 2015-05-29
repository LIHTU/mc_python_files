import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import anyio.seg7 as display
import RPi.GPIO as GPIO

BUTTON = 4
LED_PINS = [10,22,25,8,7,9,11,15] #ORDER IMPORTANT

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

ON = False
display.setup(GPIO, LED_PINS, ON)

mc = minecraft.Minecraft.create()

def bomb(x, y, z):
    mc.setBlock(x+1, y, z+1, block.TNT.id)
    for t in range(6):
        display.write(str(5-t)) # clever countdown
        time.sleep(1)

    mc.postToChat("BANG!")
    mc.setBlocks(x-10, y-5, z-10, x+10, y+10, z+10, block.AIR.id)

try:
    while True:
        time.sleep(0.1)
        if GPIO.input(BUTTON) == False:
            pos = mc.player.getTilePos()
            bomb(pos.x, pos.y, pos.z)

finally:
    GPIO.cleanup()

