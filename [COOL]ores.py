from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import keyboard

def ores_generation(block_id: int, height_down: int, height_up: int, cluster="middle"):

    import random

    x, y, z = mc.player.getTilePos()
    air = 0
    stone = 1

    if cluster == "big":
        size = 15
    elif cluster == "middle":
        size = 10
    elif cluster == "small":
        size = 5

    mc.setBlocks(x, height_down, z,
                 x+size, height_up, z+size, block_id)

    # идеальный баланс - big и size**3*5
    air_blocks = 0
    while air_blocks <= size**3*5:
        air_blocks += 1
        air_x = random.randint(x, x+size)
        air_y = random.randint(height_down, height_up)
        air_z = random.randint(z, z+size)
        mc.setBlock(air_x, air_y, air_z, stone)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            ores_generation(169, 5, 15, "big")
