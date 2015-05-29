import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import RPi.GPIO as GPIO
import random
# import blockAlphabet as 

printButton = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(printButton, GPIO.IN)

ON = False


mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

'''
Writes message in blocks
will keep track of letters position
1st letter's bottom left corner is is
    15 blocks east of playerPosition and 2 blks above.
2nd letter is 15 blks east, 2 above, and 6 south
3rd letter is 15 blks east, 2 ablove, and 12 south
etc...
'''

# define printing time delays
lil = 0.2   # for setBlock
norm = 0.5  # for setBlocks

def printBlocks(x, y, z, string):
    length = len(string)
    
    # clearpath for letters
    clearLength = (length*6)+2
    clearDepth = 6
    clearHeight = 8
    mc.setBlocks(x-(clearDepth/2),y-1,z-1,x+(clearDepth/2),y+7,z+clearLength-1, block.AIR.id)
    
    for i in range(length):
        if string[i] == 'a' or string[i] == 'A':
            # perahps store letters in blockAlphabet, then call blockAlphabet.letterA(x,y,z)
            letterA(x,y,z)

        if string[i] == 'h' or string[i] == 'H':
            letterH(x,y,z)

        if string[i] == 'i' or string[i] == 'I':
            letterI(x,y,z)

        if string[i] == 'r' or string[i] == 'R':
            letterR(x,y,z)

        if string[i] == 's' or string[i] == 'S':
            letterS(x,y,z)

        if string[i] == '!':
            letterExc(x,y,z)
            
        # set 'cursor' for next letter
        z=z+6
           
def letterA(x,y,z):
    c=random.randint(0,15)
    Asegs = [[x, y, z, x, y+5, z],
             [x, y+6, z+1, x, y+6, z+3],
             [x, y, z+4, x, y+5, z+4],
             [x, y+3, z+1, x, y+3, z+3]]
    for seg in Asegs:
        mc.setBlocks(seg, block.WOOL.id, c)
        time.sleep(norm)

def letterH(x,y,z):
    c=random.randint(0,15)
    Hsegs = [[x,y,z,x,y+6,z],
             [x,y+3,z+1,x,y+3,z+3],
             [x,y,z+4,x,y+6,z+4]]
    for seg in Hsegs:
        mc.setBlocks(seg, block.WOOL.id,c)
        time.sleep(norm)

def letterI(x,y,z):
    c=random.randint(0,15)
    Isegs = [[x,y+6,z,x,y+6,z+4],
             [x,y+5,z+2,x,y+1,z+2],
             [x,y,z,x,y,z+4]]
    for seg in Isegs:
        mc.setBlocks(seg, block.WOOL.id,c)
        time.sleep(norm)

def letterR(x,y,z):
    c=random.randint(0,15)
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

def letterS(x,y,z):
    c=random.randint(0,15)
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

def letterExc(x,y,z):
    c=random.randint(0,15)
    Excsegs = [[x,y+6,z+2,x,y+2,z+2],
             [x,y,z+2]]
    
    for seg in Excsegs:
        if len(seg) == 6:
            mc.setBlocks(seg, block.WOOL.id,c)
        if len(seg) == 3:
            mc.setBlock(seg, block.WOOL.id,c)
        time.sleep(lil)

try:
    while True:
        time.sleep(0.1)
        if GPIO.input(printButton) == False:
            pos = mc.player.getTilePos()
            printBlocks(pos.x+20, pos.y+2, pos.z, 'hi sara!!!')

finally:
    GPIO.cleanup()


