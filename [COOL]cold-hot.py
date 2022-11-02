from mcpi.minecraft import Minecraft
import math
import time
import random

mc = Minecraft.create()
pos = mc.player.getPos()
destX = pos.x + random.randint(-100, 100)
destZ = pos.z + random.randint(-100, 100)
destY = mc.getHeight(destX, destZ)

block = 57
mc.setBlock(destX, destY, destZ, block)
mc.postToChat("Блок создан")

while True:
	pos = mc.player.getPos()
	distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
	if distance > 100:
		mc.postToChat("Замерзнешь")
	elif distance > 50:
		mc.postToChat("Холодно")
	elif distance > 25:
		mc.postToChat("Тепло")
	elif distance > 12:
		mc.postToChat("Горячо")
	elif distance > 6:
		mc.postToChat("Обожжешься!")
	elif distance > 2:
		mc.postToChat("Блок найден")
		break
		quit()
	time.sleep(1)