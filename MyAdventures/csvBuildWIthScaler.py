import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

GAP = block.AIR.id
WALL = block.SNOW_BLOCK.id,1
FLOOR = block.WOOD.id,0

FILENAME = "maze1.csv"
f = open(FILENAME, "r")

''' experiment with the origins.
    take out the +1 on the z and x coords
    and see what happens when the maze is built on top of the player!
    RESULT:  if you build it on Steve, he gets frozen inside of a
    block and can't break out!
    '''

# use the scaler variable to multiply the size of your maze!
# A value of 1 will make it normal size.
# A value of 3 will make it three times as big!
# It's been tested up to a value of 20, try bigger!!
SCALER = 4

pos = mc.player.getTilePos()
ORIGIN_X = pos.x+1
ORIGIN_Y = pos.y
ORIGIN_Z = pos.z+1

z = ORIGIN_Z

for line in f.readlines():
    data = line.split(",")
    x = ORIGIN_X
    for cell in data:
        if cell == "0":
            b = GAP
        else:
            if cell == "0":
                b = GAP
                break
            b = WALL
        mc.setBlocks(x, ORIGIN_Y, z,x+SCALER,ORIGIN_Y+(SCALER*2)-1,z+SCALER, b)
        mc.setBlocks(x, ORIGIN_Y-1, z, x+SCALER,ORIGIN_Y-1,z+SCALER, FLOOR)
        x = x+SCALER
    z = z+SCALER
            
