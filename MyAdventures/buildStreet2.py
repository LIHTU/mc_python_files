import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc = minecraft.Minecraft.create()

SIZE = 10
    
def House():
    # define axes of house
    midx = x + SIZE/2
    midy = y + SIZE/2

    # Create Solid block
    w = random.randint(0, 2)
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.SANDSTONE.id, w)
    mc.setBlocks(x+1, y, z+1, x+SIZE-1, y+SIZE-1, z+SIZE-1, block.AIR.id)

    # clear door
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

    # Add two windows
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)

    # add a wooden roof
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE,block.WOOD.id)

    # add a 'random' woollen carpet
    c = random.randint(0,3)
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-1, y-1, z+SIZE-1,block.WOOL.id, c)

pos = mc.player.getTilePos()

x = pos.x+2
y = pos.y
z = pos.z

for h in range(5):
    House()
    x=x + SIZE
