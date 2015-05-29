'''
consider adding morr postToChat lines
and time delays so that we can see a
description of what's happening in the programming
while the object is being printed.
'''

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

FILENAME = "object1.csv"

def print3D(filename, originx, originy, originz):
    f = open(filename, 'r')
    lines = f.readlines()

    coords = lines[0].split(",")
    mc.postToChat('size [x y z] = '+str(coords)) # added by robin to view as list 
    sizex = int(coords[0])
    sizey = int(coords[1])
    sizez = int(coords[2])

    lineidx = 1 #loop control variable

    for y in range(sizey):
        mc.postToChat(str(y))
        lineidx = lineidx + 1

        for x in range(sizex):
            line = lines[lineidx]
            lineidx = lineidx + 1
            data = line.split(",")
            for z in range(sizez):
                blockid = int(data[z])
                mc.setBlock(originx+x, originy+y, originz+z, blockid)
                time.sleep(.1)

pos = mc.player.getTilePos()
print3D(FILENAME, pos.x+3, pos.y, pos.z+3)
