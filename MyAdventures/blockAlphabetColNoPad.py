# block alphabet random color
# defines letters and some symbols
# max char height = 7
# max char width = 5
# builds letters in ALL CAPS, so far.

'''
Writes message in blocks
will keep track of letters position
1st letter's bottom left corner is is
    15 blocks east of playerPosition and 2 blks above.
2nd letter is 15 blks east, 2 above, and 6 south
3rd letter is 15 blks east, 2 ablove, and 12 south
etc...
'''

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

# define printing time delays
lil = 0.1   # for setBlock
norm = 0.1  # for setBlocks

def printBlocks(x, y, z, string, color):
    length = len(string)
    
    # clearpath for letters
    #clearLength = (length*6)+2
    #clearDepth = 6
    #clearHeight = 8
    #mc.setBlocks(x-(clearDepth/2),y-1,z-1,
                 #x+(clearDepth/2),y+7,z+clearLength-1, block.AIR.id)
    
    for i in range(length):
        if string[i] == 'a' or string[i] == 'A':
            letterA(x,y,z,color)

        if string[i] == 'e' or string[i] == 'E':
            letterE(x,y,z,color)

        if string[i] == 'h' or string[i] == 'H':
            letterH(x,y,z,color)

        if string[i] == 'i' or string[i] == 'I':
            letterI(x,y,z,color)

        if string[i] == 'r' or string[i] == 'R':
            letterR(x,y,z,color)

        if string[i] == 's' or string[i] == 'S':
            letterS(x,y,z,color)

        if string[i] == 't' or string[i] == 'T':
            letterT(x,y,z,color)

        if string[i] == 'w' or string[i] == 'W':
            letterW(x,y,z,color)

        if string[i] == '!':
            letterExc(x,y,z,color)
            
        # set 'cursor' for next letter
        z=z+6

def letterA(x,y,z,color):
    c=color
    Asegs = [[x, y, z, x, y+5, z],
             [x, y+6, z+1, x, y+6, z+3],
             [x, y, z+4, x, y+5, z+4],
             [x, y+3, z+1, x, y+3, z+3]]
    for seg in Asegs:
        mc.setBlocks(seg, block.WOOL.id, c)
        time.sleep(norm)

def letterE(x,y,z,color):
    Esegs = [[x,y,z,x,y+6,z],
             [x,y+6,z+1,x,y+6,z+4],
             [x,y+3,z+1,x,y+3,z+3],
             [x,y,z+1,x,y,z+4]
             ]
    for seg in Esegs:
        mc.setBlocks(seg, block.WOOL.id, color)
        time.sleep(norm)

def letterH(x,y,z,color):
    c=color
    Hsegs = [[x,y,z,x,y+6,z],
             [x,y+3,z+1,x,y+3,z+3],
             [x,y,z+4,x,y+6,z+4]]
    for seg in Hsegs:
        mc.setBlocks(seg, block.WOOL.id,c)
        time.sleep(norm)

def letterI(x,y,z,color):
    c=color
    Isegs = [[x,y+6,z,x,y+6,z+4],
             [x,y+5,z+2,x,y+1,z+2],
             [x,y,z,x,y,z+4]]
    for seg in Isegs:
        mc.setBlocks(seg, block.WOOL.id,c)
        time.sleep(norm)

def letterR(x,y,z,color):
    c=color
    Rsegs = [[x,y,z,x,y+6,z],
             [x,y+6,z+1,x,y+6,z+3],
             [x,y+5,z+4,x,y+4,z+4],
             [x,y+3,z+1,x,y+3,z+3],
             [x,y+2,z+2],
             [x,y+1,z+3],
             [x,y,z+4]]
    
    for seg in Rsegs:
        if len(seg) == 6:
            mc.setBlocks(seg, block.WOOL.id,c)
        if len(seg) == 3:
            mc.setBlock(seg, block.WOOL.id,c)
        time.sleep(lil)

def letterS(x,y,z,color):
    c=color
    Ssegs = [[x,y+5,z+4],
             [x,y+6,z+1,x,y+6,z+3],
             [x,y+4,z,x,y+5,z],
             [x,y+3,z+1,x,y+3,z+3],
             [x,y+2,z+4,x,y+1,z+4],
             [x,y,z+1,x,y,z+3],
             [x,y+1,z]]
    
    for seg in Ssegs:
        if len(seg) == 6:
            mc.setBlocks(seg, block.WOOL.id,c)
            time.sleep(norm)
        if len(seg) == 3:
            mc.setBlock(seg, block.WOOL.id,c)
            time.sleep(lil)

def letterT(x,y,z,color):
    c=color
    Tsegs = [[x,y+6,z,x,y+6,z+4],
             [x,y+5,z+2,x,y,z+2]]
    for seg in Tsegs:
        mc.setBlocks(seg, block.WOOL.id,c)
        time.sleep(norm)

def letterW(x,y,z,color):
    c=color
    Wsegs = [[x,y+1,z,x,y+6,z],
             [x,y,z+1],
             [x,y+1,z+2,x,y+4,z+2],
             [x,y,z+3],
             [x,y+1,z+4,x,y+6,z+4]]
    for seg in Wsegs:
        if len(seg) == 6:
            mc.setBlocks(seg, block.WOOL.id,c)
            time.sleep(norm)
        if len(seg) == 3:
            mc.setBlock(seg, block.WOOL.id,c)
            time.sleep(lil)

def letterExc(x,y,z,color):
    c=color
    Excsegs = [[x,y+6,z+2,x,y+2,z+2],
             [x,y,z+2]]
    
    for seg in Excsegs:
        if len(seg) == 6:
            mc.setBlocks(seg, block.WOOL.id,c)
        if len(seg) == 3:
            mc.setBlock(seg, block.WOOL.id,c)
        time.sleep(lil)
