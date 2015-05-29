import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

#one
def one():
    mc.setBlocks(pos.x+8, pos.y, pos.z-1, pos.x+8, pos.y+6, pos.z+5, block.WOOL.id, 0)
    mc.setBlock(pos.x+8, pos.y+3, pos.z+2, block.WOOL.id, 15)

#two
def two():
    mc.setBlocks(pos.x+8, pos.y, pos.z-1, pos.x+8, pos.y+6, pos.z+5, block.WOOL.id, 0)
    mc.setBlock(pos.x+8, pos.y+1, pos.z, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+5, pos.z+4, block.WOOL.id, 15)

#three
def three():
    mc.setBlocks(pos.x+8, pos.y, pos.z-1, pos.x+8, pos.y+6, pos.z+5, block.WOOL.id, 0)
    mc.setBlock(pos.x+8, pos.y+1, pos.z, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+3, pos.z+2, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+5, pos.z+4, block.WOOL.id, 15)

# four
def four():
    mc.setBlocks(pos.x+8, pos.y, pos.z-1, pos.x+8, pos.y+6, pos.z+5, block.WOOL.id, 0)
    mc.setBlock(pos.x+8, pos.y+1, pos.z, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+5, pos.z, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+1, pos.z+4, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+5, pos.z+4, block.WOOL.id, 15)

#five
def five():
    mc.setBlocks(pos.x+8, pos.y, pos.z-1, pos.x+8, pos.y+6, pos.z+5, block.WOOL.id, 0)
    mc.setBlock(pos.x+8, pos.y+1, pos.z, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+5, pos.z, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+3, pos.z+2, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+1, pos.z+4, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+5, pos.z+4, block.WOOL.id, 15)

# six
def six():
    mc.setBlocks(pos.x+8, pos.y, pos.z-1, pos.x+8, pos.y+6, pos.z+5, block.WOOL.id, 0)
    mc.setBlock(pos.x+8, pos.y+1, pos.z, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+3, pos.z, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+5, pos.z, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+1, pos.z+4, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+3, pos.z+4, block.WOOL.id, 15)
    mc.setBlock(pos.x+8, pos.y+5, pos.z+4, block.WOOL.id, 15)

# counts down from three, then shows a random dice face
def randomRoll():
    three()
    time.sleep(1)
    two()
    time.sleep(1)
    one()
    time.sleep(1)
    r = random.randint(1,6)
    if r == 1:
        one()
    if r == 2:
        two()
    if r == 3:
        three()
    if r == 4:
        four()
    if r == 5:
        five()
    if r == 6:
        six()

randomRoll()
    

