# Welcome Home - door mat

import mcpi.minecraft as minecraft
import time


mc = minecraft.Minecraft.create()
lastPos = 0

while True:
    pos1 = mc.player.getTilePos()
    time.sleep(1)
    pos2 = mc.player.getTilePos()
    
    if pos2.x == 258 and pos2.y == 53 and pos2.z == 230 and pos1 != pos2:
        mc.postToChat('welcome home')
