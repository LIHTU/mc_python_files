import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
import blockAlphabet as alpha

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

alpha.printBlocks(pos.x+20, pos.y+2, pos.z, 'ehi sara!!!')
        



