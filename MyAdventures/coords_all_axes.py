# all axes tutorial

# This program will:
# clear blocks above 0,0,0
# place floor at 0,0,0
# place walls 100 blocks away in each direction
# place 5 block grid on ceiling
# set the player to 0,0,0
# 

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()
