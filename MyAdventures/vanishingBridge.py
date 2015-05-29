import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

bridge = []

def buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y-1,pos.z)

    if b== block.AIR.id or b== block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)
        coordinate = [pos.x, pos.y-1, pos.z]
        bridge.append(coordinate)
    elif b != block.GLASS.id:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
            time.sleep(0.25)
            
        
while True:
    time.sleep(0.03)
    buildBridge()
