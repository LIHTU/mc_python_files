# it would be fun to use random to decide whether the player would be punished
# with water or lava.

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import csvLetters
import random

mc = minecraft.Minecraft.create()

WIDTH = 40
finished = False

# origin points.  These will determin the where the middle of the arena is.
# It's best if they are zero!
ORGx = 0
ORGy = 0
ORGz = 0

'''
# initialize time delays (used to make testing quicker!)
one = 1
two = 2
three = 3
four = 4
five = 5
ten = 10
#will be 20
loong = 20
# will be 30
half = 30
minute = 60
'''

# initialize time delays (used to make testing quicker!)
one = .5
two = .5
three = .5
four = .5
five = .5
ten = .5
loong = .5
half = .5
minute = .5

# clear cube at origin
def reset_floor():
    mc.setBlocks(ORGx-WIDTH,0,ORGz-WIDTH,ORGx+WIDTH,0,ORGz+WIDTH,block.Block(155).id)

def clear_origin():
    # walls, floor
    mc.setBlocks(ORGx-WIDTH-1,1-1,ORGz-WIDTH-1,
                 ORGx+WIDTH+1,ORGy+62,ORGz+WIDTH+1,block.Block(155).id)
    # air
    mc.setBlocks(ORGx-WIDTH,1,ORGz-WIDTH,
                 ORGx+WIDTH,ORGy+100,ORGz+WIDTH,block.AIR.id)

def make_troughs():
    # z = 1
    mc.setBlocks(ORGx-WIDTH,ORGy+1,ORGz+1,
                 ORGx+WIDTH,ORGy+1,ORGz+1,block.Block(155).id)
    # z = -1
    mc.setBlocks(ORGx-WIDTH,ORGy+1,ORGz-1,
                 ORGx+WIDTH,ORGy+1,ORGz-1,block.Block(155).id)

def draw_points():
    # origin
    mc.setBlock(0,0,0,block.WOOL.id,15)
    mc.setBlock(0,1,1,block.WOOL.id,15)
    mc.setBlock(0,1,-1,block.WOOL.id,15)
    # intervals along x axis and troughs
    for i in range(5,WIDTH,5):
        mc.setBlock(i,0,0,block.WOOL.id,14)
        mc.setBlock(i,1,1,block.WOOL.id,14)
        mc.setBlock(i,1,-1,block.WOOL.id,14)
    for i in range(-5,WIDTH*-1,-5):
        mc.setBlock(i,0,0,block.WOOL.id,14)
        mc.setBlock(i,1,1,block.WOOL.id,14)
        mc.setBlock(i,1,-1,block.WOOL.id,14)

# east west signs
def draw_words():
    csvLetters.buildLetters(WIDTH, ((WIDTH/2)-2), -7*3+1, 'south', 'east,+x','red')
    # cuurently builds on top of east
    csvLetters.buildLetters(WIDTH*-1, ((WIDTH/2)-2), 7*3-1, 'north', 'west,-x', 'red')

def writeNorthSouth1():
    # clear old north and south signs
    mc.setBlocks(-WIDTH,5,-WIDTH,WIDTH,WIDTH,-WIDTH,block.AIR.id)
    mc.setBlocks(-WIDTH,5,WIDTH,WIDTH,WIDTH,WIDTH,block.AIR.id)
    # write north south
    time.sleep(.2)
    csvLetters.buildLetters(1-(len('north')*7)/2,WIDTH/2-2,-WIDTH,'east','north','blue')
    time.sleep(.2)
    csvLetters.buildLetters((len('south')*7)/2,WIDTH/2-2,WIDTH,'west','south','blue')

def writeNorthSouth2():
    # clear old north and south signs
    mc.setBlocks(-WIDTH,5,-WIDTH,WIDTH,WIDTH,-WIDTH,block.AIR.id)
    mc.setBlocks(-WIDTH,5,WIDTH,WIDTH,WIDTH,WIDTH,block.AIR.id)
    time.sleep(.2)
    csvLetters.buildLetters(1-(len('north,-z')*7)/2,WIDTH/2-2,-WIDTH,'east','north,-z','blue')
    time.sleep(.2)
    csvLetters.buildLetters((len('south,+z')*7)/2,WIDTH/2-2,WIDTH,'west','south,+z','blue')

def destroyTrough():
    mc.setBlocks(WIDTH*-1,1,-1,WIDTH,1,1,block.AIR.id)
    
def drawRedLines():
    # x axis
    mc.setBlocks(0,0,WIDTH*-1,0,0,WIDTH,block.WOOL.id,15)
    # y axis
    mc.setBlocks(WIDTH*-1,0,0,WIDTH,0,0,block.WOOL.id,15)
    # red towards east
    for i in range(5,WIDTH+1,5):
        mc.setBlocks(i,0,WIDTH,i,0,WIDTH*-1,block.WOOL.id,14)
    # red towards west
    for i in range(-5,(WIDTH*-1)-1,-5):
        mc.setBlocks(i,0,WIDTH*-1,i,0,WIDTH,block.WOOL.id,14)

def drawBlueLines():
    # blue lines, latitude
    for i in range(WIDTH*-1,WIDTH+1,5):
        mc.setBlocks(-WIDTH,0,i,WIDTH,0,i,block.WOOL.id,11)
    # y axis
    mc.setBlocks(0,0,WIDTH*-1,0,0,WIDTH,block.WOOL.id,15)
    # x axis
    mc.setBlocks(WIDTH*-1,0,0,WIDTH,0,0,block.WOOL.id,15)

def spawnLavaTub():
    # build obsidian block
    mc.setBlocks(-3,10,-7,3,11,-13,block.STONE.id)
    # clear tub
    mc.setBlocks(-2,11,-8,2,12,-12,block.AIR.id)
    # fill with lava
    mc.setBlocks(-2,11,-8,2,11,-12,block.LAVA.id)

def spawnWaterTub():
    # build obsidian block
    mc.setBlocks(-3,10,-7,3,11,-13,block.STONE.id)
    # clear tub
    mc.setBlocks(-2,11,-8,2,12,-12,block.AIR.id)
    # fill with lava
    mc.setBlocks(-2,11,-8,2,11,-12,block.WATER.id)

def clearLavaTub():
    mc.setBlocks(-3,10,-7,3,12,-13,block.AIR.id)

# To place ladder on column set ladder blocks(65) to the north of the column
# and use id 1.
def buildLadder(height):
    mc.setBlocks(0,1,1,0,height,1,block.STONE.id)
    mc.setBlocks(0,1,0,0,height,0,block.Block(65).id,3)

def clearLadder(height):
    mc.setBlocks(0,1,1,0,height,1,block.AIR.id)

# demolish ladder by breaking off 3 block chunks from top every half second.
def demolishLadder(height):
    for i in range(height,1,-3):
        mc.setBlocks(0,i,1,0,i-2,1,block.AIR.id)
        time.sleep(.5)

def buildGreenBox(x1,y1,z1,x2,y2,z2):
    mc.setBlocks(x1,y1,z1,x2,y2,z2,block.WOOL.id,13)
    mc.setBlock(x1,y1,z1,block.WOOL.id,4)
    mc.setBlock(x2,y2,z2,block.WOOL.id,6)

def destroyBox(x1,y1,z1,x2,y2,z2):
    mc.setBlocks(x1,y1,z1,x2,y2,z2,block.AIR.id)

def buildOrangeBox(x1,y1,z1,x2,y2,z2):
    mc.setBlocks(x1,y1,z1,x2,y2,z2,block.WOOL.id,1)
    mc.setBlock(x1,y1,z1,block.WOOL.id,4)
    mc.setBlock(x2,y2,z2,block.WOOL.id,6)

def spawnTNT():
    mc.setBlock(0,1,-10,block.TNT.id,1)
    mc.setBlock(0,2,-10,block.FIRE.id)
    time.sleep(10)
    mc.setBlock(0,2,-10,block.AIR.id)

# SETUP
# clear arena if not made, use 0,10,0 as test block
tenBlock = mc.getBlock(0,10,0)
wallBlock = mc.getBlock(0,1,WIDTH+1)
if tenBlock != block.AIR.id or wallBlock != block.Block(155).id:
    clear_origin()

# Break origin block to reset on next build
originBlock = mc.getBlock(0,0,0)
if originBlock == block.AIR.id:
    clear_origin()

tubBlock = mc.getBlock(0,10,-10)
if tubBlock != block.AIR.id:
    clearLavaTub()

ladderBlock = mc.getBlock(0,2,-1)
if ladderBlock != block.AIR.id:
    clearLadder()
    mc.setBlock(0,1,-1, block.WOOL.id,15)

# build stuff
reset_floor()
make_troughs()
draw_points()
draw_words()
mc.player.setTilePos(0,1,0)


# post directions
time.sleep(one)
mc.postToChat('Press F3 on your keyboard')
time.sleep(three)
mc.postToChat('Look for the line called "Block:"')
time.sleep(five)
mc.postToChat('This displays your x, y, z coordinates')
time.sleep(ten)
mc.postToChat("For now we'll just look at the first number.")
time.sleep(five)
mc.postToChat("The first number is your x coordinate.")
time.sleep(five)
mc.postToChat("Stand at the center of the arena. The numbers after block should be 0 1 0.")
time.sleep(five)
mc.postToChat("If not, use the command 'setworldspawn 0 0 0' and restart the coordinates game.")


# delay to allow them to look around, walk around, get used to looking at coords in F3.
# set to 20 for activity.
time.sleep(loong)

# declare answer variables
answerRed = 0
happensEast = 0
answerEast = 0
eastWallLoc = str(WIDTH+1)
answerWest = 0
westWallLoc = str((WIDTH*-1)-1)
blueLineStart = random.randint(WIDTH*-1, WIDTH-7)
blueLineEnd = blueLineStart+6
answerBlue1 = 0
answerBlue2 = 0
ladderAnswer = 0
ladderHeight = 0
northAnswer = 0
greenRectAnswer1 = 0
greenRectAnswer2 = 0
orangeRectAnswer1 = 0
orangeRectAnswer2 = 0
greenBoxAnswer1 = 0
greenBoxAnswer2 = 0

while not finished:
    
    # what happens as you walk East question
    while happensEast != 'bigger':
        mc.postToChat('What happens to your x coordinate as you walk towards the EAST wall?')
        time.sleep(three)
        mc.postToChat('Does it get bigger or smaller?')
        time.sleep(three)
        mc.postToChat('Type bigger or smaller in the console.')
        time.sleep(one)
        mc.postToChat('To switch to the console, hold the Alt key and press Tab.')
        
        happensEast = raw_input('Does your X coordinate get bigger or smaller as you go east? Type "bigger" or "smaller": ')
        if happensEast == 'bigger':
            mc.postToChat("bigger, huh?  Let me check...")
            time.sleep(three)
            mc.postToChat("That's right!!!")
            time.sleep(three)
        elif happensEast == 'smaller':
            spawnWaterTub()
            mc.postToChat('Sorry, that is wrong.')
            time.sleep(two)
            mc.postToChat('You must be punished.')
            time.sleep(one)
            mc.postToChat('Careful! On the next question it will be filled with lava!')
            mc.player.setTilePos(0,20,-10)
            time.sleep(four)
            happensEast = ''
        else:
            spawnWaterTub()
            mc.postToChat('Sorry, that is wrong.')
            time.sleep(two)
            mc.postToChat('You must be punished.')
            time.sleep(one)
            mc.postToChat('Careful! On the next question it will be filled with lava!')
            mc.player.setTilePos(0,20,-10)
            time.sleep(four)
            happensEast = ''
    
    # marker question
    while answerRed != '5':
        mc.postToChat('How frequent are the red markers?')
        time.sleep(three)
        mc.postToChat('Answer in the Python Console')
        time.sleep(one)
        mc.postToChat('It would be best if you answered correctly :)')
        answerRed = raw_input("If you're standing on one red marker, how far do you have to walk to be standing on another one? ")
        if answerRed == '5':
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
            mc.postToChat("Let me get rid of these walls and extend these red markers.")
            destroyTrough()
            time.sleep(two)
            drawRedLines()
            # extend the sleep to 20 or so so they can walk around a bit more.
            mc.postToChat('Notice as you walk along a red line your x coordinate stays the same.')
            time.sleep(ten)
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('You must be punished.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)
    
    
    # east wall question
    while answerEast != eastWallLoc:
        mc.postToChat('At what x coordinate is the east wall?')
        answerEast = raw_input('At what x coordinate is the east wall? ')
        if answerEast == eastWallLoc:
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('You must be punished.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)

    # west wall question
    while answerWest != westWallLoc:
        mc.postToChat('At what x coordinate is the west wall?')
        answerWest = raw_input('At what x coordinate is the west wall? ')
        if answerWest == westWallLoc:
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Next contestant, please.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)

    # Blue LineStart Question
    while answerBlue1 !=  str(blueLineStart):
        mc.setBlocks(blueLineStart,0,-1,blueLineStart+6,0,-1,block.WOOL.id,11)
        mc.postToChat('I just drew a blue line on the floor.')
        mc.postToChat('Where does the blue line start? (lowest x coord)')
        answerBlue1 = raw_input("Where does the blue line start? What's it's lowest x coordinate?): ")
        if answerBlue1 == str(blueLineStart):
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Maybe dying will help you think better...')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)

    # Blue LineEnd Question
    while answerBlue2 != str(blueLineEnd):
        mc.postToChat('Where does the blue line end?')
        answerBlue2 = raw_input("Type in the x coord where the blue line ends: ")
        if answerBlue2 == str(blueLineEnd):
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
            mc.postToChat("Let's erase this blue line.")
            time.sleep(one)
            reset_floor()
            drawRedLines()
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Time for a hot bath.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)
    
    firstTry = True
    ladder = False
    
    # Ladder Time!
    while ladderAnswer != str(ladderHeight):
        while firstTry == True:
            mc.postToChat("Now let's figure out y coordinates.")
            time.sleep(three)
            mc.postToChat("The second number in the 'Block' line is your y coordinate.")
            time.sleep(five)
            mc.postToChat("The y coordinate tells you your vertical position in the world.")
            time.sleep(five)
            mc.postToChat("In other words it tells you your elevation or distance from the bottom of the world.")
            time.sleep(five)
            mc.postToChat("Watch what your y coordinate does when you jump up and down.")
            time.sleep(five)
            mc.postToChat("Let's build a ladder.")
            time.sleep(three)
        
            while not ladder:
                mc.postToChat("How tall do you want the ladder to be?")
                time.sleep(three)
                mc.postToChat("Type a number into the console.")
                ladderHeight = int(raw_input('Enter a number between 10 and 50: '))
                if ladderHeight >= 10 and ladderHeight <=50:
                    buildLadder(ladderHeight)
                    ladder = True
                    time.sleep(2)
                else:
                    mc.postToChat('Please enter a number between 10 and 50.')
                
            mc.postToChat("Done!")
            time.sleep(two)
            mc.postToChat("Climb around on the ladder.")
            time.sleep(five)
            mc.postToChat("What happens to your y coordinate value as you go up?")
            time.sleep(ten)
            mc.postToChat("Do you x and z coordinates change at all?")
            time.sleep(five)
            firstTry = False

        mc.postToChat("What's the y coordinate of the top ladder segment?")
        ladderAnswer = raw_input("What's the y coordinate of the top ladder segment?")
        if ladderAnswer == str(ladderHeight):
            mc.postToChat("Correct!!!")
            time.sleep(two)
            demolishLadder(ladderHeight)
        else:
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Time for a hot bath.')
            spawnLavaTub()
            time.sleep(one)
            mc.player.setTilePos(0,20,-10) 
            time.sleep(5)
            clearLavaTub()

    # North Wall
    while northAnswer != 'negative':
        writeNorthSouth1()
        drawBlueLines()
        mc.postToChat("Finally, time for z coordinates!")
        time.sleep(two)
        mc.postToChat("The z coordinate is the third number in the 'Block' line.")
        time.sleep(five)
        mc.postToChat("Is the north wall in the z positive direction, or the z negative direction?")
        northAnswer = raw_input("Type in 'positive' or 'negative': ")
        if northAnswer == 'negative':
            mc.postToChat("You are right!")
            clearLavaTub()
            writeNorthSouth2()
        elif northAnswer[0] == 'n' and northAnswer != 'negative':
            spawnLavaTub()
            mc.postToChat('Looks like you need to work on spelling.')
            time.sleep(two)
            mc.postToChat('Lava Time for you!')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Time for a hot bath.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)
    
    # Green Rectangle
    while greenRectAnswer1 != '12,12':
        buildGreenBox(12,0,12,20,0,25)
        mc.postToChat('I just made a green rectangle on the floor!')
        time.sleep(two)
        mc.postToChat('Go find it!')
        time.sleep(four)
        mc.postToChat('At what x and z coordinates is the yellow corner?')
        time.sleep(two)
        mc.postToChat('Type in the two numbers with a comma in between, like this "1,2"')
        greenRectAnswer1 = raw_input('Type in the x and z coordinates of the yellow corner: ')
        if greenRectAnswer1 == '12,12':
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Oh well, lava is a great teacher.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)

    while greenRectAnswer2 != '20,25':
        mc.postToChat('At what x and z coordinates is the pink corner?')
        time.sleep(two)
        mc.postToChat('Type in the two numbers with a comma in between, like this "13,17"')
        greenRectAnswer2 = raw_input('Type in the x and z coordinates of the pink corner: ')
        if greenRectAnswer2 == '20,25':
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Oh well, lava is a great teacher.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)

    #Orange Rectangle
    while orangeRectAnswer1 != '-5,0,5':
        buildOrangeBox(-5,0,5,5,0,15)
        mc.postToChat('I just made an orange rectangle!')
        time.sleep(two)
        mc.postToChat('At what x,y,z coordinates is the yellow corner?')
        time.sleep(two)
        mc.postToChat('Type in the three numbers with a comma in between, like this "5,6,7"')
        orangeRectAnswer1 = raw_input('Type in the x,y,z coordinates of the yellow corner: ')
        if orangeRectAnswer1 == '-5,0,5':
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
        elif orangeRectAnswer1[3] == '1':
            mc.postToChat("Wrong answer, but I'll let you off easy this time.")
            time.sleep(one)
            mc.postToChat("Remember that the floor is one y coordinate below you!")
            time.sleep(four)
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Oh well, lava is a great teacher.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)

    while orangeRectAnswer2 != '5,0,15':
        mc.postToChat('At what x,y,z coordinates is the pink corner?')
        time.sleep(two)
        orangeRectAnswer2 = raw_input('Type in the x,y,z coordinates of the pink corner: ')
        if orangeRectAnswer2 == '5,0,15':
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
            reset_floor()
            drawRedLines()
            drawBlueLines()
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Oh well, lava is a great teacher.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)

    while greenBoxAnswer1 != '10,1,10':
        buildGreenBox(10,1,10,20,10,20)
        mc.postToChat("I just made a green box.")
        time.sleep(four)
        mc.postToChat("At what coordinates is the yellow corner?")
        greenBoxAnswer1 = raw_input('Type in the x,y,z coordinates of the yellow corner: ')
        if greenBoxAnswer1 == '10,1,10':
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Oh well, lava is a great teacher.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)

    while greenBoxAnswer2 != '20,10,20':
        pos = mc.player.getTilePos()
        mc.setBlocks(15,1,9,15,10,9,block.Block(65).id,3)
        mc.postToChat("At what coordinates is the pink corner?")
        greenBoxAnswer2 = raw_input('Type in the x,y,z coordinates of the pink corner: ')
        if greenBoxAnswer2 == '20,10,20':
            mc.postToChat("Correct!!!")
            clearLavaTub()
            time.sleep(two)
            destroyBox(10,1,10,20,10,20)
            mc.postToChat("Great work!")
            time.sleep(three)
            mc.postToChat("You've finished the game!")
            time.sleep(three)
            mc.postToChat("Now go bake yourself a cake!")
            Finished = True
        else:
            spawnLavaTub()
            mc.postToChat('Wrong Answer.')
            time.sleep(two)
            mc.postToChat('Oh well, lava is a great teacher.')
            time.sleep(one)
            mc.player.setTilePos(0,20,-10)
