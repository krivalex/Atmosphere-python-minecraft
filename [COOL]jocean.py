from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

time.sleep(5)

width = 150
height = 4
length = 150

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

shwrX = x
shwrY = y
shwrZ = z

# создается сзади слева


if shwrX <= x < shwrX + width \
		and shwrY <= y < shwrY + height \
		and shwrZ <= z < shwrZ + length:
	mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 8)
	time.sleep(10)
else:
	mc.setBlocks(shwrX, shwrY + height,
				 shwrZ, shwrX + width,
				 shwrY + height, shwrZ + length, 0)