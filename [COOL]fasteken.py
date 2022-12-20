from mcpi.minecraft import Minecraft

import random
import time

mc = Minecraft.create()

min_player_x, min_player_y, min_player_z = mc.player.getTilePos()

size = 15

max_player_x = min_player_x + size
max_player_y = min_player_y + size
max_player_z = min_player_z + size

blocks = []


def delete(x, y, z):
    mc.setBlock(x, y, z, 0)


def create_game_one():

    for x in range(size):
        blocks.append([])
        for z in range(size):
            blocks[x].append((35, random.randint(0, 15)))

    for x in range(size):
        for z in range(size):
            mc.setBlock(min_player_x+x, 115, min_player_z +
                        z, blocks[x][z][0], blocks[x][z][1])
            z += 1
        x += 1

    mc.player.setTilePos(min_player_x + x//2, 116, min_player_z+z//2)
    return blocks


def create_game_two():
    for x in range(size):
        blocks.append([])
        for z in range(size):
            blocks[x].append((35, z))

    for x in range(size):
        for z in range(size):
            mc.setBlock(min_player_x+x, 115, min_player_z +
                        z, blocks[x][z][0], blocks[x][z][1])
            z += 1
        x += 1

    mc.player.setTilePos(min_player_x + x//2, 116, min_player_z+z//2)
    return blocks


def game_logic():
    create_game_one()

    blocks_type = [(35, 0), (35, 1), (35, 2), (35, 3), (35, 4), (35, 5),
                   (35, 6), (35, 7), (35, 8), (35, 9), (35, 10), (35, 11),
                   (35, 12), (35, 13), (35, 14), (35, 15)]

    blocks_name = ["Белый", "Оранжевый", "Пурпурный", "Голубой", "Желтый", "Лаймовый",
                   "Розовый", "Серый", "Светло-серый", "Бирюзовый", "Фиолетовый", "Синий",
                   "Коричневый", "Темно-зеленый", "Красный", "Черный"]

    while True:
        game_color_name = random.choice(blocks_name)
        game_block_color_index = blocks_name.index(game_color_name)
        game_color_block = blocks_type[game_block_color_index]

        mc.postToChat("Встань на блок " + game_color_name.capitalize())
        time.sleep(3)

        for x in range(size):
            for z in range(size):
                if blocks[x][z] != game_color_block:
                    delete(min_player_x+x, 115, min_player_z+z)
                z += 1
            x += 1

        time.sleep(1)
        create_game_one()


game_logic()
