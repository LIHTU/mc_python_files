import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
size = int(raw_input('size of area to clear? '))

mc.setBlocks(pos.x+1, pos.y, pos.z+1, pos.x+size, pos.y-size, pos.z+size, block.AIR.id)
