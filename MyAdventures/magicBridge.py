import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

def buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y-1,pos.z)

    if b== block.AIR.id or b== block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)
        
while True:
    time.sleep(0.2)
    buildBridge()
