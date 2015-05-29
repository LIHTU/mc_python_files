import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

mc = minecraft.Minecraft.create()

horseBlocks = [minecraftstuff.ShapeBlock(0,0,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(-1,0,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(1,0,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(-1,-1,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(1,-1,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(1,1,0,block.WOOD_PLANKS.id),
               minecraftstuff.ShapeBlock(2,1,0,block.WOOD_PLANKS.id)]

horsePos = mc.player.getTilePos()
horsePos.z = horsePos.z+1
horsePos.y = horsePos.y+1

horseShape = minecraftstuff.MinecraftShape(mc, horsePos, horseBlocks)

for count in range(1,10):
    time.sleep(1)
    horseShape.moveBy(1,0,0)
horseShape.clear()
time.sleep(3)
# use the draw function to recreate the horse at it's last location.
horseShape.draw()
