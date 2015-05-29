# Hello Ilana
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import mcpi.minecraftstuff as minecraftstuff
import csvLettersCopy as csvLetters

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
orientation = 'na'


while True:
    direction = mc.player.getDirection()
    if direction.x > .71:
        orientation = 'east'
    if direction.x < -.71:
        orientation = 'west'
    if direction.z < -.71:
        orientation = 'north'
    if direction.z > .71:
        orientation = 'south'
    
    mc.postToChat(str(round(direction.x,2))+ ' '+
                  str(round(direction.y,2))+ ' '+
                  str(round(direction.z,2)))
    time.sleep(.5)
    mc.postToChat(orientation)
    
    time.sleep(1)
