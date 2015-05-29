# Welcome Home - door mat

import mcpi.minecraft as minecraft
import time


mc = minecraft.Minecraft.create()
lastPos = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    
    if pos.x == 258 and pos.y == 53 and pos.z == 230:
        mc.postToChat('welcome home')
