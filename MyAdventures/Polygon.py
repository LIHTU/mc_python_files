import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()

points = []

# triangle
points.append(minecraft.Vec3(pos.x, pos.y, pos.z))
points.append(minecraft.Vec3(pos.x + 20, pos.y, pos.z))
points.append(minecraft.Vec3(pos.x +10, pos.y + 20, pos.z))

mcdrawing.drawFace(points, True, block.WOOL.id, 6)
points = []

# hexagon
points.append(minecraft.Vec3(pos.x, pos.y, pos.z+10))
points.append(minecraft.Vec3(pos.x - 5, pos.y + 8, pos.z+10))
points.append(minecraft.Vec3(pos.x, pos.y + 16, pos.z+10))
points.append(minecraft.Vec3(pos.x + 8, pos.y +16, pos.z+10))
points.append(minecraft.Vec3(pos.x +13, pos.y + 8, pos.z+10))
points.append(minecraft.Vec3(pos.x +8, pos.y, pos.z+10))

mcdrawing.drawFace(points, True, block.WOOL.id, 6)
