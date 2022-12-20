from tqdm import tqdm

import keyboard
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2


def copyStructure(x1, y1, z1, x2, y2, z2):

    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    sctructure = []
    print("Создание структуры...")

    for y in tqdm(range(height)):
        sctructure.append([])
        for z in range(length):
            sctructure[y].append([])
            for x in range(width):
                sctructure[y][z].append(mc.getBlock(x1 + x, y1 + y, z1 + z))

    return sctructure


def buildScrtucture():
    while not keyboard.is_pressed('up'):
        print("Выберите первую точку")
        x1, y1, z1 = mc.player.getTilePos()
    while not keyboard.is_pressed('down'):
        print("Выберите вторую точку")
        x2, y2, z2 = mc.player.getTilePos()

    structure = copyStructure(x1, y1, z1, x2, y2, z2)

    while not keyboard.is_pressed('left'):
        print("Выберите точку для постройки")
        x, y, z = mc.player.getTilePos()

    yStart = y
    xStart = x
    zStart = z

    for y in tqdm(range(len(structure))):
        for z in range(len(structure[y])):
            for x in range(len(structure[y][z])):
                time.sleep(0.05)
                mc.setBlock(xStart + x, yStart + y,
                            zStart + z, structure[y][z][x])


buildScrtucture()
