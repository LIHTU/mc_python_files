import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

floor = str(raw_input('would you like a floor? y/n'))

if floor == 'y':
    size = int(raw_input('size of area to clear? '))
    mc.setBlocks(pos.x-(size/2), pos.y, pos.z-(size/2),
             pos.x+(size/2), pos.y+5, pos.z+(size/2),
             block.AIR.id)
    mc.setBlocks(pos.x-(size/2), pos.y-1, pos.z-(size/2),
             pos.x+(size/2), pos.y-1, pos.z+(size/2),
             block.SANDSTONE.id)

if floor == 'n':
    size = int(raw_input('size of area to clear? '))
    mc.setBlocks(pos.x-(size/2), pos.y, pos.z-(size/2),
             pos.x+(size/2), pos.y+5, pos.z+(size/2),
             block.AIR.id)
