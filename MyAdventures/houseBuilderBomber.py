import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import anyio.seg7 as display
import RPi.GPIO as GPIO

bombButton = 4
houseButton = 14
LED_PINS = [10,22,25,8,7,9,11,15] #ORDER IMPORTANT

GPIO.setmode(GPIO.BCM)
GPIO.setup(bombButton, GPIO.IN)
GPIO.setup(houseButton, GPIO.IN)

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
    newPos = mc.player.getTilePos()
    if newPos.x > x-size and newPos.x<x+size and newPos.y>(y-size/2) and newPos.y<y+size and newPos.z>z-size and newPos.z<z+size:
        # tp player above bomb site
        mc.player.setPos(x,y+size,z)

    mc.postToChat("BANG!")
    mc.setBlocks(x-size, y-(size/2), z-size, x+size, y+size*2, z+size, block.AIR.id)

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
        if GPIO.input(bombButton) == False:
            pos = mc.player.getTilePos()
            bomb(pos.x, pos.y, pos.z)
            
        if GPIO.input(houseButton) == False:
            pos = mc.player.getTilePos()
            SIZE = 18
            x = pos.x - (SIZE/2)
            y = pos.y - 1
            z = pos.z - (SIZE/2)
            house()
            

finally:
    GPIO.cleanup()

