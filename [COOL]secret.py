import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x_door = -366
y_door = 78
z_door = -68

x_block = -371
y_block = 81
z_block = -68

mc.player.setTilePos(x_door, y_door, z_door)

air = 0
stone = 1

time.sleep(3)
gift = mc.getBlock(x_block, y_block, z_block)

open = True
while True:

    while gift == 57:
        gift = mc.getBlock(x_block, y_block, z_block)
        mc.setBlocks(x_door, y_door, z_door,
                     x_door - 2, y_door + 2, z_door + 2,
                     air)
        if open:
            mc.postToChat("Дверь открыта")
            open = False
    while gift != 57:
        gift = mc.getBlock(x_block, y_block, z_block)
        mc.postToChat("Вставьте ключ")
        mc.setBlocks(x_door, y_door, z_door,
                     x_door - 2, y_door + 2, z_door + 2,
                     stone)