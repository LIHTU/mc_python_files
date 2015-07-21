# Adventure 7: LinesCirclesAndSpheres.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, SIZE14
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

#create the minecraft api
mc = minecraft.Minecraft.create()

#create the minecraft drawing object
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

SIZE = 25;

#draw 3 lines
def draw3lines():
    pos = mc.player.getTilePos()
    mcdrawing.drawLine(pos.x, pos.y, pos.z, pos.x, pos.y+SIZE, pos.z, block.WOOL.id,1)
    mcdrawing.drawLine(pos.x, pos.y, pos.z, pos.x+SIZE, pos.y, pos.z, block.WOOL.id,2)
    mcdrawing.drawLine(pos.x, pos.y, pos.z, pos.x + SIZE, pos.y + SIZE, pos.z, block.WOOL.id, 3)
    time.sleep(1)
    
#draw a circle above the player
def circle():
    pos = mc.player.getTilePos()
    mcdrawing.drawCircle(pos.x, pos.y + SIZE, pos.z, SIZE, block.WOOL.id, 4)
    time.sleep(1)

def sphere():
    pos = mc.player.getTilePos()
    mcdrawing.drawSphere(pos.x, pos.y + SIZE, pos.z, SIZE, block.WOOL.id, 5)
    time.sleep(1)

draw3lines()
circle()
sphere()
