import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import math
import time

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

while True:
    pos = mc.player.getTilePos()
    mc.postToChat(str(pos.x)+' '+str(pos.y)+' '+str(pos.z))
    time.sleep(1)
