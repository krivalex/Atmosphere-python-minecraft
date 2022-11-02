import keyboard
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def growTree(count_of_trees, size_of_forest):
    import random
    x, y, z = mc.player.getTilePos()
    count = 0

    while count <= count_of_trees:
        count += 1

        random_bias_wood_x = random.randint(-size_of_forest, size_of_forest)
        random_bias_wood_z = random.randint(-size_of_forest, size_of_forest)

        tree_x = x + random_bias_wood_x
        tree_z = z + random_bias_wood_z
        tree_y = mc.getHeight(tree_x, tree_z)

        wood = 17, 0
        leaf = 18, 0
        light = 169

        wood_tree_height = tree_y + 5
        leaf_first_stage = 3
        leaf_second_stage = 2
        leaf_third_stage = 1

        mc.setBlocks(tree_x, tree_y, tree_z,
                     tree_x, wood_tree_height, tree_z, wood)
        mc.setBlocks(tree_x-leaf_first_stage, wood_tree_height, tree_z-leaf_first_stage,
                     tree_x+leaf_first_stage, wood_tree_height, tree_z+leaf_first_stage, leaf)
        mc.setBlocks(tree_x-leaf_second_stage, wood_tree_height+1, tree_z-leaf_second_stage,
                     tree_x+leaf_second_stage, wood_tree_height+1, tree_z+leaf_second_stage, leaf)
        mc.setBlocks(tree_x-leaf_third_stage, wood_tree_height+2, tree_z-leaf_third_stage,
                     tree_x+leaf_third_stage, wood_tree_height+2, tree_z+leaf_third_stage, leaf)
        mc.setBlock(tree_x, tree_y+7, tree_z, light)

if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            growTree(100, 100)
