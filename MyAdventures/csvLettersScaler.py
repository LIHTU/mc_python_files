import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

gap = block.AIR.id
let = block.WOOL.id,14

# use the scaler variable to multiply the size of your maze!
# A value of 1 will make it normal size.
# A value of 3 will make it three times as big!
# It's been tested up to a value of 20, try bigger!!
SCALER = 0

pos = mc.player.getTilePos()
ORIGIN_X = pos.x+1
ORIGIN_Y = pos.y
ORIGIN_Z = pos.z+1

z = ORIGIN_Z

'''
Steps
1. create printLetters function that will take and input string
and read through it like printBlocks
1.5 create control structure for direction
2. create control structure that calls different letter functions depending
on what character the string is on.
3. create fucntion for each letter that calls a csv file
'''

# because of color argument, may only work on blocks with a block id
# but may it works with any block if color is passed as 0
def printLetters(x,y,z,direction,string,color):
    length = len(string)

    for let in range(length):
        if string[let] == 'a' or string[let] == 'A':
            Asouth(x,y,z,color)

    # set 'cursor' for next letter
        z=z+6

def Asouth(x,y,z,color)
    FILENAME = "A.csv"
    f = open(FILENAME, "a")

    for line in f.readlines():
        data = line.split(",")
        x = ORIGIN_X
        for cell in data:
            if cell == "0":
                b = gap
            else:
                # why are these three lines here?
                #if cell == "0":
                    #b = gap
                    #break
                b = let
            mc.setBlocks(x, ORIGIN_Y, z,x+SCALER,ORIGIN_Y+SCALER,-1,z+SCALER, b)
            x = x+SCALER
        z = z+SCALER
