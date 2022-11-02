from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing, MinecraftShape, MinecraftTurtle
from mcpi import block
import time

mc = Minecraft.create()

pos = mc.player.getTilePos()

steve = MinecraftTurtle(mc, pos)

steve.penblock(169)

steve.forward(15)

steve.left(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.left(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.left(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.left(90)
steve.forward(15)

steve.right(90)
steve.forward(15)