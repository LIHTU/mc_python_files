import mcpi.minecraft as minecraft
import mcpi.block as block # modules which holds constant numbers for all block types

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
mc.setBlock(pos.x+3, pos.y+5, pos.z, block.AIR.id)
