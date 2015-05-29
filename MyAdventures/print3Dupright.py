'''
consider adding more postToChat lines
and time delays so that we can see a
description of what's happening in the programming
while the object is being printed.
'''

'''
Consider modifying the program so that it prints the
top of the csv at the top in game instead of at the
bottom.
'''

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

FILENAME = "object1.csv"

def getDimensions(filename):
    f = open(filename, 'r')
    lines = f.readlines()

    coords = lines[0].split(",")
    mc.postToChat('size [x y z] = '+str(coords)) # added by robin to view as list 
    yscale = int(coords[1])
    mc.postToChat('yscale = ' + str(yscale))
    return yscale

def print3D(filename, originx, originy, originz):
    f = open(filename, 'r')
    lines = f.readlines()

    coords = lines[0].split(",")
    sizex = int(coords[0])
    sizey = int(coords[1])
    sizez = int(coords[2])

    lineidx = 1 #loop control variable
    mc.postToChat('intro')

    # loops from sizey down to zero, instead of from 0 to size y
    # and build from above the player down to the player's level.
    for y in range(sizey,0,-1):
        mc.postToChat(str(y))
        lineidx = lineidx + 1
        mc.postToChat('for y')

        for x in range(sizex):
            line = lines[lineidx]
            lineidx = lineidx + 1
            data = line.split(",")
            mc.postToChat('for x')

            for z in range(sizez):
                blockid = int(data[z])
                mc.setBlock(originx+x, originy+y, originz+z, blockid)
                time.sleep(.1)
                mc.postToChat('for z')


pos = mc.player.getTilePos()
yscale = getDimensions(FILENAME)
print3D(FILENAME, pos.x+3, pos.y, pos.z+3)
