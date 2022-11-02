from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    pos = mc.player.getPos()
    for i in range(5):
        mc.setBlock(pos.x, pos.y, pos.z, 38, 1)
        mc.setBlock(pos.x + i, pos.y, pos.z + i, 38, 2)
        mc.setBlock(pos.x + i, pos.y, pos.z, 38, 3)
        mc.setBlock(pos.x, pos.y, pos.z + i, 38, 4)
        mc.setBlock(pos.x - i, pos.y, pos.z, 38, 5)
        mc.setBlock(pos.x, pos.y, pos.z - i, 38, 6)
        mc.setBlock(pos.x - i, pos.y, pos.z - i, 38, 7)
        mc.setBlock(pos.x + i, pos.y, pos.z - i, 38, 8)
        mc.setBlock(pos.x - i, pos.y, pos.z + i, 38, 9)
        time.sleep(0.1)
