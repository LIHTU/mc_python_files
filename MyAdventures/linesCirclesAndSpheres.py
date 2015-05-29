import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

mc = minecraft.Minecraft.create()

mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()

mcdrawing.drawLine(pos.x, pos.y, pos.z,
                   pos.x, pos.y + 20, pos.z,
                   block.WOOL.id, 1)

mcdrawing.drawLine(pos.x, pos.y, pos.z,
                   pos.x + 20, pos.y, pos.z,
                   block.WOOL.id, 2)

mcdrawing.drawLine(pos.x, pos.y, pos.z,
                   pos.x +20, pos.y +20, pos.z,
                   block.WOOL.id, 3)

time.sleep(5)

pos = mc.player.getTilePos()

mcdrawing.drawCircle(pos.x + 20, pos.y + 20, pos.z, 20,
                    block.WOOL.id, 4)

time.sleep(5)

pos = mc.player.getTilePos()

mcdrawing.drawSphere(pos.x, pos.y +20, pos.z, 15,
                     block.WOOL.id, 5)

