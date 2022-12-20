# миссия: создаем радужную пирамиду Атмосферы
import keyboard
import time
from mcpi.minecraft import Minecraft
# импортируем клавиатуру
# подключаемся к серверу
mc = Minecraft.create()

# создаем функция которая будет генерировать пирамиду
# передаем аргументами тип блока и высоту пирамиды


def pyramid(block: int, height: int):
  # получаем координаты игрока
    x, y, z = mc.player.getTilePos()
    x, y, z = x + height, y, z

  # задаем переменную для цвета
    color = -1

    # цикл для генерации пирамиды
    for level in reversed(range(height)):
      # создаем конструкцию для обновления цвета
        if color > 15:
            color = 0
        color += 1

        # устанавливаем блоки
        mc.setBlocks(x - level, y, z - level, x +
                     level, y, z + level, block, color)
        # увеличиваем высоту
        y += 1


# запускаем бесконечный цикл
while True:
  # запускаем функцию при нажатии клавиши q
    if keyboard.is_pressed("q"):
        pyramid(block=35, height=180)
  # останавливаем цикл при нажатии клавиши m
    elif keyboard.is_pressed("m"):
        break
