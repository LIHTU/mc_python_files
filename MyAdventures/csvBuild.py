# Intended for designing and building 2D objects along the ground

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

GAP = block.AIR.id
WALL = block.GOLD_BLOCK.id
FLOOR = block.GRASS.id

FILENAME = "maze1.csv"
f = open(FILENAME, "r")

''' experiment with the origins.
    take out the +1 on the z and x coords
    and see what happens when the maze is built on top of the player!
    RESULT:  if you build it on Steve, he gets frozen inside of a
    block and can't break out!
    '''

pos = mc.player.getTilePos()
ORIGIN_X = pos.x+1
ORIGIN_Y = pos.y
ORIGIN_Z = pos.z+1

z = ORIGIN_Z

# How could we multiply the scale of the maze?
for line in f.readlines():
    data = line.split(",")
    x = ORIGIN_X
    for cell in data:
        if cell == "0":
            b = GAP
        else:
            b = WALL
        mc.setBlock(x, ORIGIN_Y, z, b)
        mc.setBlock(x, ORIGIN_Y+1, z, b)
        mc.setBlock(x, ORIGIN_Y+2, z, b) # added to make walls higher :)
        mc.setBlock(x, ORIGIN_Y-1, z, FLOOR)
        x = x+1
    z = z+1
            
