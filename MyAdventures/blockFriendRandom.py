import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import math
import time
import random

#function get the distance between 2 points
def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

#constants
# how far away the block has to be before he stops following
TOO_FAR_AWAY = 15

#create minecraft and minecraftstuff objects
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#set the blocks mood
blockMood = "happy"

#create the block next to the player
friend = mc.player.getTilePos()
friend.x = friend.x + 5
# find out the height of the world at x, y, so the friend is on top
friend.y = mc.getHeight(friend.x, friend.z)
# create the block 
mc.setBlock(friend.x, friend.y, friend.z, block.DIAMOND_BLOCK.id)
# say hello
mc.postToChat("<block> Hello friend")
# the friends target is where he currently is
target = friend.clone()

while True:
    pos = mc.player.getTilePos()
    distance = distanceBetweenPoints(pos, friend)
    #apply the rules to work out where the block should be doing next
    # am I happy?
    if blockMood == "happy":
        #where is the player?  Are they near enough to me or should I move to them?
        if distance < TOO_FAR_AWAY:
            target = pos.clone()
        if distance >= TOO_FAR_AWAY:
            blockMood = "sad"
            mc.postToChat("<block> Come back. You are too far away. I need a hug!")

    elif blockMood == "sad":
        if distance <= 1:
            blockMood = "happy"
            mc.postToChat("<block> Awww thanks. Lets go.")
        if random.randint(1,100) == 100:
            blockMood = "hadenough"
            mc.postToChat("<block> That's it. I have had enough.")
            

    #move block to the target
    if friend != target:
        #get the blocks in between block friend and player, by 'drawing' an imaginary line
        blocksBetween = mcdrawing.getLine(friend.x, friend.y, friend.z,
                                          target.x, target.y, target.z)
        #loop through the blocks in between the friend and the target
        # loop to the last but 1 block (:-1) otherwise the friend will be sitting on top of the player
        for blockBetween in blocksBetween[:-1]:
            mc.setBlock(friend.x, friend.y, friend.z, block.AIR.id)
            friend = blockBetween.clone()
            friend.y = mc.getHeight(friend.x, friend.z)
            mc.setBlock(friend.x, friend.y, friend.z, block.DIAMOND_BLOCK.id)
            time.sleep(0.25)
        # we have reached our target, so set the target to be friend's position
        target = friend.clone()

    #sleep for a little bit to give the computer a rest!
    time.sleep(0.25)
    
