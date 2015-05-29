import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
import random
import thread
import anyio.seg7 as display
import anyio.GPIO as GPIO

BUTTON = 4
LED_PINS = [7,6,14,16,10,8,9,15]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
ON = False # common-anode, set to True for common cathode
display.setup(GPIO, LED_PINS, ON)

#arena constants
ARENAX = 20
ARENAZ = 30
ARENAY = 5
RIVERWIDTH = 6

def createArena(pos):
    mc = minecraft.Minecraft.create()
    pos.x
    mc.setBlocks(pos.x - 1, pos.y, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y - 3,
                 pos.z + ARENAZ + 1, block.GRASS.id)
    mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y + ARENAY, pos.z + ARENAZ + 1,
                 block.GLASS.id)
    mc.setBlocks(pos.x, pos.y +1, pos.z,
                 pos.x + ARENAX, pos.y + ARENAY,
                 pos.z + ARENAZ, block.AIR.id)

def theWall(arenaPos, wallZPos):
    mc = minecraft.Minecraft.create()
    wallPos = minecraft.Vec3(arenaPos.x, arenaPos.y + 1, arenaPos.z + wallZPos)
    wallBlocks = []
    for x in range(0, ARENAX + 1):
        for y in range(1, ARENAY):
            wallBlocks.append(minecraftstuff.ShapeBlock(x, y, 0,
                                                        block.BRICK_BLOCK.id))
    wallShape = minecraftstuff.MinecraftShape(mc, wallPos, wallBlocks)
    while not gameOver:
        wallShape.moveBy(0,1,0)
        time.sleep(1)
        wallShape.moveBy(0,-1,0)
        time.sleep(1)
                

def theRiver(arenaPos, riverZPos):
    mc = minecraft.Minecraft.create()
    global RIVERWIDTH
    RIVERWIDTH = 8
    BRIDGEWIDTH = 2

    mc.setBlocks(arenaPos.x, arenaPos.y - 2,
                 arenaPos.z + riverZPos,
                 arenaPos.x + ARENAX, arenaPos.y,
                 arenaPos.z + riverZPos + RIVERWIDTH - 1,
                 block.AIR.id)
    
    mc.setBlocks(arenaPos.x, arenaPos.y - 2,
                 arenaPos.z + riverZPos,
                 arenaPos.x + ARENAX, arenaPos.y - 2,
                 arenaPos.z + riverZPos + RIVERWIDTH - 1,
                 block.WATER.id)

    bridgePos = minecraft.Vec3(arenaPos.x, arenaPos.y,
                               arenaPos.z + riverZPos +1)
    bridgeBlocks = []
    for x in range(0, BRIDGEWIDTH):
        for z in range(0, RIVERWIDTH -2):
            bridgeBlocks.append(minecraftstuff.ShapeBlock(x, 0, z,
                                                      block.WOOD_PLANKS.id))
    bridgeShape = minecraftstuff.MinecraftShape(mc, bridgePos, bridgeBlocks)
    steps = ARENAX - BRIDGEWIDTH +1

    while not gameOver:
        for left in range(0, steps):
            bridgeShape.moveBy(1,0,0)
            time.sleep(1)
        for right in range(0, steps):
            bridgeShape.moveBy(-1,0,0)
            time.sleep(1)
    
def theHoles(arenaPos, holesZPos):
    mc = minecraft.Minecraft.create()

    HOLES = 80
    HOLESWIDTH = 12

    while not gameOver:
        holes = []
        for count in range(0, HOLES):
            # x coord will have a random value between x-edges of the arena
            x = random.randint(arenaPos.x,
                               arenaPos.x + ARENAX)
            z = random.randint(arenaPos.z + holesZPos,
                               arenaPos.z + holesZPos + HOLESWIDTH)
            holes.append(minecraft.Vec3(x, arenaPos.y, z))
            
        for hole in holes:
            mc.setBlock(hole.x, hole.y, hole.z,
                        block.WOOL.id, 14)
        time.sleep(0.5)
        
        for hole in holes:
            mc.setBlocks(hole.x, hole.y, hole.z,
                        hole.x, hole.y - 1, hole.z,
                        block.AIR.id)
            # Lava bonus
            mc.setBlock(hole.x, hole.y-2, hole.z,
                        block.LAVA.id)
        time.sleep(1)

        for hole in holes:
            mc.setBlocks(hole.x, hole.y, hole.z,
                        hole.x, hole.y - 3, hole.z,
                        block.GRASS.id)
        time.sleep(2)

def createDiamonds(arenaPos, number):
    mc = minecraft.Minecraft.create()

    for diamond in range(0, number):
        x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
        z = random.randint(arenaPos.z, arenaPos.z + ARENAZ)
        mc.setBlock(x, arenaPos.y +1, z, block.DIAMOND_BLOCK.id)
        

mc = minecraft.Minecraft.create()
gameOver = False

arenaPos = mc.player.getTilePos()
arenaPos.x -= ARENAX/2
arenaPos.y -= 1
arenaPos.z -= 1
createArena(arenaPos)

RIVERZ = 4
thread.start_new_thread(theRiver, (arenaPos, RIVERZ))

WALLZ = RIVERZ + RIVERWIDTH + 3
thread.start_new_thread(theWall, (arenaPos, WALLZ))

HOLESZ = WALLZ + 5
thread.start_new_thread(theHoles, (arenaPos, HOLESZ))

LEVELS = 3
DIAMONDS = [3,5,9]
TIMEOUTS = [8,30,30]

level = 0
points = 0

mc.postToChat("Press the button to start")
while GPIO.input(BUTTON):
    time.sleep(0.1)

#game loop
while not gameOver:
    
    createDiamonds(arenaPos, DIAMONDS[level])
    diamondsLeft = DIAMONDS[level]
    display.write(str(diamondsLeft))

    start = time.time()
    levelComplete = False

    #level loop
    while not gameOver and not levelComplete:
        pos = mc.player.getTilePos()
        if pos.y < arenaPos.y:
            mc.player.setPos(arenaPos.x + ARENAX/2, arenaPos.y + 1,
                             arenaPos.z + 1)
        if pos.z == arenaPos.z + ARENAZ and diamondsLeft == 0:
            levelComplete = True
        
        secondsLeft = TIMEOUTS[level] - (time.time() - start)
        if secondsLeft < 5:
            display.setdp(True)
        else:
            display.setdp(False)
        if secondsLeft < 0:
            gameOver = True
            mc.postToChat("Out of Time!")
            
        hits = mc.events.pollBlockHits()
        for hit in hits:
            blockHitType = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
            if blockHitType == block.DIAMOND_BLOCK.id:
                mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z,
                            block.AIR.id)
                diamondsLeft = diamondsLeft - 1
                display.write(str(diamondsLeft))

        if levelComplete:
            points = points +(DIAMONDS[level] * int(secondsLeft))
            mc.postToChat("Level Complete - Points = " + str(points))
            level = level + 1
            if level == LEVELS:
                gameOver = True
                mc.postToChat("Congratulations - All levels complete")
        
        time.sleep(0.1)

mc.postToChat("Game Over - Points = " + str(points))
display.clear()
GPIO.cleanup()
