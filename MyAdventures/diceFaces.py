import mcpi.minecraft as minecraft
import mcpi.block as block

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

three()

