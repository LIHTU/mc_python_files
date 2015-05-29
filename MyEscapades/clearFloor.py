import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
size = int(raw_input('size of area to clear? '))
height = int(raw_input('height of area to clear? '))

mc.setBlocks(pos.x-(size/2), pos.y, pos.z-(size/2),
             pos.x+(size/2), pos.y+height, pos.z+(size/2),
             block.AIR.id)
