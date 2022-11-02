import keyboard

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def destroy(size_x: int, size_y: int, size_z: int):

    x,y,z = mc.player.getTilePos()
    air = 0

    mc.setBlocks(x, y, z, x+size_x, y+size_y, z+size_z, air)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            destroy(100, 30, 100)