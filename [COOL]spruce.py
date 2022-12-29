from mcpi import minecraft
import minecraftstuff
from threading import Thread

import time
import keyboard
import random

mc = minecraft.Minecraft.create()


spruce_block = 17, 1
tree_leave_3 = 159, 13

gold = 41
emerald = 133
snow = 78
big_snow = 80

all_toys = []


def tree(size):

    global Star

    start_x, start_y, start_z = mc.player.getTilePos()
    pos = mc.player.getTilePos()

    # листва
    tree_y = start_y
    for stage in reversed(range(size)):
        mc.setBlocks(start_x-stage, tree_y+3, start_z-stage,
                     start_x+stage, tree_y+3, start_z+stage, tree_leave_3)
        mc.setBlocks(start_x-stage, tree_y+4, start_z-stage,
                     start_x+stage, tree_y+4, start_z+stage, snow)
        tree_y += 1

        for i in range(45):
            toy_x = random.randint(start_x-stage, start_x+stage)
            toy_z = random.randint(start_z-stage, start_z+stage)
            mc.setBlock(toy_x, tree_y+3, toy_z, 35, random.randint(0, 15))
            all_toys.append([toy_x, tree_y+3, toy_z])

    # ствол
    mc.setBlocks(start_x, start_y, start_z, start_x,
                 start_y+size, start_z, spruce_block)
    mc.setBlocks(start_x-3, start_y, start_z-3, start_x+3,
                 start_y+3, start_z+3, spruce_block)

    # подарки
    mc.setBlocks(start_x-3, start_y, start_z-3,
                 start_x-5, start_y+2, start_z-5, 35, 4)
    mc.setBlocks(start_x+3, start_y, start_z-3,
                 start_x+5, start_y+2, start_z-5, 35, 5)
    mc.setBlocks(start_x-3, start_y, start_z+3,
                 start_x-5, start_y+2, start_z+5, 35, 6)
    mc.setBlocks(start_x+3, start_y, start_z+3,
                 start_x+5, start_y+2, start_z+5, 35, 7)

    # звезда

    star_list = [

        minecraftstuff.ShapeBlock(0, 0+size+4, 0, gold),
        minecraftstuff.ShapeBlock(0, 1+size+4, 0, gold),
        minecraftstuff.ShapeBlock(0, 2+size+4, 0, emerald),
        minecraftstuff.ShapeBlock(0, 3+size+4, 0, gold),
        minecraftstuff.ShapeBlock(0, 4+size+4, 0, gold),

        minecraftstuff.ShapeBlock(1, 1+size+4, 0, gold),
        minecraftstuff.ShapeBlock(1, 2+size+4, 0, gold),
        minecraftstuff.ShapeBlock(1, 3+size+4, 0, gold),

        minecraftstuff.ShapeBlock(2, 0+size+4, 0, gold),
        minecraftstuff.ShapeBlock(2, 2+size+4, 0, gold),
        minecraftstuff.ShapeBlock(2, 4+size+4, 0, gold),

        minecraftstuff.ShapeBlock(-1, 1+size+4, 0, gold),
        minecraftstuff.ShapeBlock(-1, 2+size+4, 0, gold),
        minecraftstuff.ShapeBlock(-1, 3+size+4, 0, gold),

        minecraftstuff.ShapeBlock(-2, 0+size+4, 0, gold),
        minecraftstuff.ShapeBlock(-2, 2+size+4, 0, gold),
        minecraftstuff.ShapeBlock(-2, 4+size+4, 0, gold),

    ]

    Star = minecraftstuff.MinecraftShape(mc, pos, star_list)

    return


def move_start():
    global Star
    time.sleep(15)
    count = 0
    while True:
        Star.rotate(count, 0, 0)
        time.sleep(0.05)
        count += 1


def move_toys():
    while True:

        print("toys are moving")

        for toy in all_toys:
            mc.setBlock(toy[0], toy[1], toy[2], 169)

        time.sleep(1)

        for toy in all_toys:
            mc.setBlock(toy[0], toy[1], toy[2], 35, random.randint(0, 15))


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("q"):
            tree(10)

            t1 = Thread(target=move_start)
            t2 = Thread(target=move_toys)
            t1.start()
            t2.start()
            # t1.join()
            # t2.join()
