# Use this file to scan any structure or area.
# It gets really slow past a size of about 10
# perhaps we could do some testing and create a size vs time graph!
# heck, while we're at we should produce that graph in the minecrat world!!
# can we build a stopwatch into our program?

# size 20 = 5.6 minutes

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# REMEMBER to change file name if you want to create a new file
# instead of overwriting an old one.
FILENAME = "towertop.csv"
SIZEX = 20
SIZEY = 20
SIZEZ = 20

def scan3D(filename, originx, originy, originz):
    f = open(filename, "w")

    f.write(str(SIZEX) + "," + str(SIZEY) + "," +str(SIZEZ) + "\n")

    for y in range(SIZEY):
        mc.postToChat('scan:' +str(y))
        mc.postToChat(str(y*1.0/SIZEY*100)+'%')
        f.write("\n")
        for x in range(SIZEX):
            line = ''
            for z in range(SIZEZ):
                blockid = mc.getBlock(originx+x, originy+y, originz+z)
                if line != "":
                    line = line + ','
                line = line + str(blockid)
            f.write(line + "\n")
    f.close()

# place player in center and at bottom of area to be scanned
pos = mc.player.getTilePos()
scan3D(FILENAME, pos.x-(SIZEX/2),pos.y, pos.z-(SIZEZ/2))
