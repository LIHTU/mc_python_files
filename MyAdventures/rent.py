import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

x1 = 0
z1 = 0
x2 = 10
z2 = 10

# coordinates of starting pad
HOME_X = x2 - ((x2-x1)/2) # in front of gate
HOME_Y = -6
HOME_Z = z1 - 2

rent = 0
inFieild = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x>x1 and pos.x < x2 and pos.z>z1 and pos.z< z2:
        rent = rent + 1
        mc.postToChat('You owe rent:'+str(rent))
        inField = inField + 1
    else: #not in the field
        inField = 0
    if inField > 3:
        mc.postToChat('Too slow!')
        # teleport player back to starting pad
        mc.player.setPos(HOME_X, HOME_Y, HOME_Z)
        
