import mcpi.minecraft as minecraft
import time
import random

mc = minecraft.Minecraft.create()

FILENAME = "tips.txt"

f = open(FILENAME, "r")

tips = f.readlines()

f.close()

while True:
    time.sleep(random.randint(3,7))
    msg = random.choice(tips)
    mc.postToChat(msg.strip())
