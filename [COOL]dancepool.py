from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from playsound import playsound
import time

pos = mc.player.getTilePos()
floorX = pos.x - 2
floorY = pos.y - 1
floorZ = pos.z - 2

width = 5
length = 5
block = 41

play = True

mc.setBlocks(floorX, floorY, floorZ, floorX + width, floorY, floorZ + length, block)
while floorX <= pos.x <= floorX + width and floorZ <= pos.z <= floorZ + length:
    if play:
        playsound('files/Song.mp3', False)
        play = False
    if block == 41:
        block = 57
    elif block == 57:
        block = 22
    elif block == 22:
        block = 133
    elif block == 133:
        block = 169
    else:
        block = 41
    mc.setBlocks(floorX, floorY, floorZ, floorX + width, floorY, floorZ + length, block)
    pos = mc.player.getTilePos()
    time.sleep(0.5)
