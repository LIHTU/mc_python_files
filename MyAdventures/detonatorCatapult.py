import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import anyio.seg7 as display
#import RPi.GPIO as GPIO #pi
import anyio.GPIO as GPIO #arduino

BUTTON = 4
LED_PINS = [10,22,25,8,7,9,11,15] #pi
LED_PINS = [7,6,14,16,10,8,9,15] #arduino

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

ON = False
display.setup(GPIO, LED_PINS, ON)

mc = minecraft.Minecraft.create()

def bomb(x, y, z):
    size = 10
    mc.setBlock(x+1, y, z+1, block.TNT.id)
    for t in range(6):
        display.write(str(5-t)) # clever countdown
        time.sleep(1)

    # tp player if inside blast radius
    pos = mc.player.getTilePos()
    if pos.x > x-size and pos.x<x+size and pos.y>(y-size/2) and pos.y<y+size and pos.z>z-size and pos.z<z+size:
        # tp player above bomb site
        mc.player.setPos(x,y+size,z)

    mc.postToChat("BANG!")
    mc.setBlocks(x-size, y-(size/2), z-size, x+size, y+size, z+size, block.AIR.id)

try:
    while True:
        time.sleep(0.1)
        if GPIO.input(BUTTON) == False:
            pos = mc.player.getTilePos()
            bomb(pos.x, pos.y, pos.z)

finally:
    GPIO.cleanup()

