# build a quiz block
# when hit it will ask a question that requires a raw input answer
# correct! answers will teleport you to a vat of lava!
# can we set and detonate tnt? or give player tnt or weapons?
# wrong answers will do nothing.

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import mcpi.minecraftstuff as minecraftstuff
import csvLetters

mc = minecraft.Minecraft.create()

WIDTH = 30
# origin
ORGx = 0
ORGy = 0
ORGz = 0

# clear cube at origin
def clear_origin():
    # walls, floor
    mc.setBlocks(ORGx-WIDTH-1,1-1,ORGz-WIDTH-1,
                 ORGx+WIDTH+1,ORGy+62,ORGz+WIDTH+1,block.Block(155).id)
    # air
    mc.setBlocks(ORGx-WIDTH,1,ORGz-WIDTH,
                 ORGx+WIDTH,ORGy+100,ORGz+WIDTH,block.AIR.id)

def make_troughs():
    # z = 1
    mc.setBlocks(ORGx-WIDTH,ORGy+1,ORGz+1,
                 ORGx+WIDTH,ORGy+1,ORGz+1,block.Block(155).id)
    # z = -1
    mc.setBlocks(ORGx-WIDTH,ORGy+1,ORGz-1,
                 ORGx+WIDTH,ORGy+1,ORGz-1,block.Block(155).id)

def draw_points():
    # origin
    mc.setBlock(0,0,0,block.WOOL.id,15)
    mc.setBlock(0,1,1,block.WOOL.id,15)
    mc.setBlock(0,1,-1,block.WOOL.id,15)
    # intervals
    for i in range(5,100,5):
        mc.setBlock(i,0,0,block.WOOL.id,14)
        mc.setBlock(i,1,1,block.WOOL.id,14)
        mc.setBlock(i,1,-1,block.WOOL.id,14)
    for i in range(-5,-100,-5):
        mc.setBlock(i,0,0,block.WOOL.id,14)
        mc.setBlock(i,1,1,block.WOOL.id,14)
        mc.setBlock(i,1,-1,block.WOOL.id,14)
    time.sleep(2)

def draw_words():
    csvLetters.buildLetters(WIDTH, ((WIDTH/2)-2), -7*3+1, 'south', 'east,+x','red')
    # cuurently builds on top of east
    csvLetters.buildLetters(WIDTH*-1, ((WIDTH/2)-2), 7*3-1, 'north', 'west,-x', 'black')

# recreate arena only if origin block isn't black wool
# this shaves 10 seconds off of program run time.
orgBlock = mc.getBlock(0,0,0)
if orgBlock != 35:
    clear_origin()
    make_troughs()
    draw_points()
    draw_words()
    
mc.player.setTilePos(0,1,0)
time.sleep(1.0)
mc.postToChat('Press F3 on your keyboard')
time.sleep(2)
mc.postToChat('This will display your x, y, z coordinates')

while True:
    pos = mc.player.getTilePos()
    #mc.postToChat('x:' + str(pos.x))
    #mc.postToChat(' y:' + str(pos.y) + ' z:' + str(pos.z))
    time.sleep(.5)

    if pos.x == 1 or pos.x == -1:
        mc.postToChat('At what x coordinates are the red markers?')
    if pos.x == 5 or pos.x == -5 or pos.x == 10 or pos.x == -10:
        mc.postToChat('x:'+str(pos.x))
    if pos.x == 10:
        mc.postToChat('At what x coordinate is the east wall?')
    if pos.x == -20:
        mc.postToChat('At what x coordinate is the west wall?')
    if pos.x == -10:
        
