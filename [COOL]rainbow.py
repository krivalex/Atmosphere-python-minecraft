import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import time
mc = minecraft.Minecraft.create()

playerPos = mc.player.getTilePos()
colors = [14, 1, 4, 5, 3, 11, 10]
height = 50

for x in range(0, 128):
    for color_index in range(0, len(colors)):
        y = playerPos.y+sin((x / 128.0) * pi) * height + color_index
        mc.setBlock(playerPos.x + x - 64, int(y), playerPos.z,
                    block.WOOL.id, colors[len(colors) - 1 - color_index])
        time.sleep(0.02)
print("rainbow created at x:{} y:{} z:{}".format(
    playerPos.x, playerPos.y, playerPos.z))
