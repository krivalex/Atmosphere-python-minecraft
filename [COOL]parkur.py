import mcpi.minecraft as minecraft
import mcpi.block as block

import time
import random

mc = minecraft.Minecraft.create()
startPos = mc.player.getTilePos()
mc.setBlock(startPos.x, 150, startPos.z, block.GOLD_BLOCK.id)
mc.player.setTilePos(startPos.x, 152, startPos.z)

mc.postToChat("Игра начнется через 5 секунд")
time.sleep(5)
mc.postToChat("Удачи! Не стой на месте!")

blocks = []
blocks_type = [(35, 14), (35, 1), (35, 4), (35, 5),
               (35, 3), (35, 11), (35, 10)]
blocks.append([startPos.x, 150, startPos.z])
maxPos = 0
color = 0

while True:

    x_random_block = random.randint(-2, 3)
    y_random_block = random.randint(0, 1)
    z_random_block = random.randint(-2, 3)

    delta_random_block = mc.player.getTilePos()
    delta_random_block.x += x_random_block
    delta_random_block.y += y_random_block-1
    delta_random_block.z += z_random_block

    if delta_random_block.x != blocks[-1][0] and delta_random_block.z != blocks[-1][2]:
        if color == 7:
            color = 0
        mc.setBlock(delta_random_block.x, delta_random_block.y,
                    delta_random_block.z, blocks_type[color])
        color += 1

    time.sleep(1)
    blocks.append(
        [delta_random_block.x, delta_random_block.y, delta_random_block.z])

    if len(blocks) > 5:
        delete_block = blocks.pop(0)
        mc.setBlock(delete_block[0], delete_block[1],
                    delete_block[2], block.AIR.id)

        pos = mc.player.getTilePos()
        mc.postToChat("Высота: " + str(pos.y))
        if pos.y > maxPos:
            maxPos = pos.y

        if pos.y < 150:
            for delete_block in blocks:
                mc.setBlock(delete_block[0], delete_block[1],
                            delete_block[2], block.AIR.id)
            mc.postToChat("Игра окончена!")
            mc.postToChat("Вы достигли " + str(maxPos) + " блоков")
            break
