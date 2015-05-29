import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

diamond_pos = mc.player.getTilePos()
diamond_pos.x = diamond_pos.x + 1
mc.setBlock(diamond_pos.x, diamond_pos.y, diamond_pos.z, block.DIAMOND_BLOCK.id)

def checkHit():
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        if pos.x == diamond_pos.x and pos.y == diamond_pos.y and pos.z == diamond_pos.z:
            mc.postToChat('HIT')
            mc.postToChat(e.face)

while True:
    time.sleep(1)
    checkHit()
