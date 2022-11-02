from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import keyboard

def func():
    block = 24
    # block = 0
    height = 100
    
    pos = mc.player.getTilePos()
    x, y, z = pos.x + height, pos.y, pos.z
    for level in reversed(range(height)):
        mc.setBlocks(x - level, y, z - level, x + level, y, z + level, block)
        y += 1

while True:
    if keyboard.is_pressed('q'):
        func()