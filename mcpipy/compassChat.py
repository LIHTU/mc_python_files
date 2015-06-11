# Compass To Chat
# the values of getDirection appear to be the cosine of the angle
# between the respective axis and the player's orientation.

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import csvLettersCopy as csvLetters

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
orientation = 'na'
lastOrientation = ''

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
    
    if lastOrientation != orientation:
        mc.postToChat(orientation)
    time.sleep(.1)
    lastOrientation = orientation

