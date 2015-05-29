import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import anyio.seg7 as display
import RPi.GPIO as GPIO

houseButton = 14
LED_PINS = [10,22,25,8,7,9,11,15] #ORDER IMPORTANT

GPIO.setmode(GPIO.BCM)
GPIO.setup(houseButton, GPIO.IN)

ON = False
display.setup(GPIO, LED_PINS, ON)

mc = minecraft.Minecraft.create()

def house():
    # define axes of house
    midx = x + SIZE/2
    midy = y + SIZE/2

    # Create Solid block
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.SANDSTONE.id)
    mc.setBlocks(x+1, y, z+1, x+SIZE-1, y+SIZE-1, z+SIZE-1, block.AIR.id)

    # clear door
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

    # Add two windows
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)

    # add a wooden roof
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE,block.WOOD.id)

    # add a woollen carpet
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-1, y-1, z+SIZE-1,block.WOOL.id, 14)

try:
    while True:
        time.sleep(0.1)
        if GPIO.input(houseButton) == False:
            pos = mc.player.getTilePos()
            SIZE = 18
            x = pos.x - (SIZE/2)
            y = pos.y - 1
            z = pos.z - (SIZE/2)
            house()

finally:
    GPIO.cleanup()

