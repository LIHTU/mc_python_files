# csvLetters
'''
This module is written for use with MCPI.
It takes in coordinates, a direction (NSEW), a string,
and a color string and builds block letters based on the string using
csv files to store the shapes of the letters.
The csv files have letters that are in all caps.  There's a couple
punctuation symbolds used as well.  It is very east to add new 2
dimensional objects by creating new .csv files and calling them.
It is also easy to add more colors.
The letter dimensions are 5 x 7

This version is written to read 0 from a csv file as an AIR block.
Any other value will produce a WOOl block of the specified color(five to
choose from).
This module could be expanded to include more conditionals (line ~ 136)
to read more values so as to allow the user to build letters out of varying
materials.  A good use of this might be to fill the csv cell with
a wool color id.  ex: (If cell == 15, b = black)

The direction parameter could be omitted, especially if one integrated
a getDirection() function so that the letters would always print in front
of the player.

The letter() fuction is a modified form of csvBuild.py in the book
"Adventures in Minecraft" by Martin O'Hanlon and David Whale.
'''

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

# definitions of block types and colors.
gap = block.AIR.id
white = block.WOOL.id,1
yellow = block.WOOL.id,4
blue = block.WOOL.id,11
brown = block.Block(35).id,12
green = block.WOOL.id,13
red = block.WOOL.id,14
black = block.WOOL.id,15


# This is the main function.  Call this function to build letters.
def buildLetters(x,y,z,direction,string,color):
    
    length = len(string)

    for character in range(length):
        
        # xFac (short for x-factor) and z Fac are used to build letters in a
        # specified direction.
        # It would be fairly east to add more diretions, such as 'southeast'
        if direction == 'south':
            xFac = 0
            zFac = 1
        if direction == 'north':
            xFac = 0
            zFac = -1
        if direction == 'east':
            xFac = 1
            zFac = 0
        if direction == 'west':
            xFac = -1
            zFac = 0
            
        if string[character] == 'a' or string[character] == 'A':
            letter(x,y,z,xFac,zFac,'A.csv',color)
        if string[character] == 'b' or string[character] == 'B':
            letter(x,y,z,xFac,zFac,'B.csv',color)
        if string[character] == 'c' or string[character] == 'C':
            letter(x,y,z,xFac,zFac,'C.csv',color)
        if string[character] == 'd' or string[character] == 'D':
            letter(x,y,z,xFac,zFac,'D.csv',color)
        if string[character] == 'e' or string[character] == 'E':
            letter(x,y,z,xFac,zFac,'E.csv',color)
        if string[character] == 'f' or string[character] == 'F':
            letter(x,y,z,xFac,zFac,'F.csv',color)
        if string[character] == 'g' or string[character] == 'G':
            letter(x,y,z,xFac,zFac,'G.csv',color)
        if string[character] == 'h' or string[character] == 'H':
            letter(x,y,z,xFac,zFac,'H.csv',color)
        if string[character] == 'i' or string[character] == 'I':
            letter(x,y,z,xFac,zFac,'I.csv',color)
        if string[character] == 'j' or string[character] == 'J':
            letter(x,y,z,xFac,zFac,'J.csv',color)
        if string[character] == 'k' or string[character] == 'K':
            letter(x,y,z,xFac,zFac,'K.csv',color)
        if string[character] == 'l' or string[character] == 'L':
            letter(x,y,z,xFac,zFac,'L.csv',color)
        if string[character] == 'm' or string[character] == 'M':
            letter(x,y,z,xFac,zFac,'M.csv',color)
        if string[character] == 'n' or string[character] == 'N':
            letter(x,y,z,xFac,zFac,'N.csv',color)
        if string[character] == 'o' or string[character] == 'O':
            letter(x,y,z,xFac,zFac,'O.csv',color)
        if string[character] == 'p' or string[character] == 'P':
            letter(x,y,z,xFac,zFac,'P.csv',color)
        if string[character] == 'q' or string[character] == 'Q':
            letter(x,y,z,xFac,zFac,'Q.csv',color)
        if string[character] == 'r' or string[character] == 'R':
            letter(x,y,z,xFac,zFac,'R.csv',color)
        if string[character] == 's' or string[character] == 'S':
            letter(x,y,z,xFac,zFac,'S.csv',color)
        if string[character] == 't' or string[character] == 'T':
            letter(x,y,z,xFac,zFac,'T.csv',color)
        if string[character] == 'u' or string[character] == 'U':
            letter(x,y,z,xFac,zFac,'U.csv',color)
        if string[character] == 'v' or string[character] == 'v':
            letter(x,y,z,xFac,zFac,'V.csv',color)
        if string[character] == 'w' or string[character] == 'W':
            letter(x,y,z,xFac,zFac,'W.csv',color)
        if string[character] == 'x' or string[character] == 'X':
            letter(x,y,z,xFac,zFac,'X.csv',color)
        if string[character] == 'y' or string[character] == 'Y':
            letter(x,y,z,xFac,zFac,'Y.csv',color)
        if string[character] == 'z' or string[character] == 'Z':
            letter(x,y,z,xFac,zFac,'Z.csv',color)
        if string[character] == ' ':
            letter(x,y,z,xFac,zFac,'space.csv',color)
        if string[character] == ',':
            letter(x,y,z,xFac,zFac,'comma.csv',color)
        if string[character] == '.':
            letter(x,y,z,xFac,zFac,'period.csv',color)
        if string[character] == '!':
            letter(x,y,z,xFac,zFac,'exclamation.csv',color)
        if string[character] == '+':
            letter(x,y,z,xFac,zFac,'positive.csv',color)
        if string[character] == '-':
            letter(x,y,z,xFac,zFac,'negative.csv',color)
            
        # set 'cursor' for next letter
        z=z+6*zFac
        x=x+6*xFac

def letter(x,y,z,xFac,zFac,FILENAME,color):
    f = open(FILENAME, "r")

    #write from the top of the csv file (top of letter), which has 7 rows
    y += 6
    
    for line in f.readlines():
        line = line.strip()
        data = line.split(",")
        for cell in data:
            #time.sleep(.5)
            #mc.postToChat(cell)
            if cell == "0":
                b = gap
            else:
                if color == 'blue':
                    b = blue
                if color == 'black':
                    b = black
                if color == 'red':
                    b = red
                if color == 'green':
                    b = green
            mc.setBlock(x,y,z,b)
            if xFac != 0:
                x = x+(1*xFac)
            if zFac != 0:
                z = z+1*zFac
        if zFac != 0:
            z-=5*zFac
        if xFac != 0:
            x-=5*xFac
        y -= 1

        
