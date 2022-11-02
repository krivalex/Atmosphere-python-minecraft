from mcpi.minecraft import Minecraft
import keyboard

mc = Minecraft.create()


def setPillar(x, y, z, height):
    """Создает колонну. Аргументы задают ее позицию и высоту"""
    stairBlock = 156
    block = 155
    # Вершина колонны
    mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1,
                 block, 1)
    mc.setBlock(x - 1, y + height - 1, z, stairBlock, 12)
    mc.setBlock(x + 1, y + height - 1, z, stairBlock, 13)
    mc.setBlock(x, y + height - 1, z + 1, stairBlock, 15)
    mc.setBlock(x, y + height - 1, z - 1, stairBlock, 14)
    # Основание колонны
    mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, block, 1)
    mc.setBlock(x - 1, y + 1, z, stairBlock, 0)
    mc.setBlock(x + 1, y + 1, z, stairBlock, 1)
    mc.setBlock(x, y + 1, z + 1, stairBlock, 3)
    mc.setBlock(x, y + 1, z - 1, stairBlock, 2)
    # Ствол колонны
    mc.setBlocks(x, y, z, x, y + height, z, block, 2)


def func():
    pos = mc.player.getTilePos()
    x, y, z = pos.x + 2, pos.y, pos.z

    for i in range(0, 100, 5):
        setPillar(x + i, y, z, 8)
        setPillar(x - i, y, z, 8)
        for j in range(0, 100, 5):
            setPillar(x, y, z+j, 8)
            setPillar(x, y, z-j, 8)

while True:
    if keyboard.is_pressed('q'):
        func()

