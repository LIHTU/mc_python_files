import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()

def place_towers():
    pos = mc.player.getTilePos()
    
    x = pos.x
    y = pos.y
    z = pos.z
    
    # center
    mc.setBlock(x,y-1,z,block.WOOD.id)

    # north/white (snow)
    mc.setBlocks(x,y,z-5,x,y+4,z-5,block.WOOL.id, 0)

    # east/yellow (sunrise)
    mc.setBlocks(x+5,y,z,x+5,y+4,z,block.WOOL.id, 4)

    # south/red (sun and heat)
    mc.setBlocks(x,y,z+5,x,y+4,z+5,block.WOOL.id, 14)

    # west/black (where the sun goes down)
    mc.setBlocks(x-5,y,z,x-5,y+4,z,block.WOOL.id, 15)

place_towers()
