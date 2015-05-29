# example string Program 
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import csvLetters

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

# if you wish you can store your string in a variable, so as to center it from
# the player's vantage point.
sampleString = "Hello Kitty!"

# build letters 20 blks east, 2 blocks up, half the length north.
x = pos.x + 20
y = pos.y + 2
z = pos.z - len(sampleString)*6/2

csvLetters.buildLetters(x,y,z,'south',sampleString,'blue')
