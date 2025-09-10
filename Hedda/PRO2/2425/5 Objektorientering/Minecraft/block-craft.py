import random
import turtle
import painter
import gameworld
import block as b

BLOCK_SIZE = 25

def on_click(x,y):
    row, col = calculate_coordinates(x,y)

    check_grid_click(row, col)
    check_inventory_click(x,y)

def check_grid_click(row, col):
    position = calculate_grid_index(row, col)
    if position >= 0:
        if game_world.blocks[position].hit(game_world.player.active_tool.strength) == False:
            game_world.update_block(position, b.Block("Air", 0,0, "white"))
            game_world.draw_world(painter)
            game_world.add_score(1)
            print("Player score:", game_world.player.score)

def check_inventory_click(row,col):
    check_tools_click(row,col)
    check_blocks_click(row,col)


def check_tools_click(row,col):
    # Detta är de
    position = calculate_tools_index(row, col)
    if position >= 0:
        game_world.player.active_tool = game_world.player.tools[position]

def check_blocks_click(row, col):
    position = calculate_blocks_index(row, col)
    if position >= 0:
        game_world.player.active_block = game_world.palyer.blocks[position]

def calculate_coordinates(x,y):
    col = int(x//BLOCK_SIZE)
    row = int(y//BLOCK_SIZE)
    return row, col

def calculate_grid_index(row, col):
    if (col < 0 or row < 0 or
        col >= game_world.width or row > game_world.height):
        return -1
    return row*game_world.width+col

def calculate_tools_index(row, col):
    if (col != -2 or
        row < 0 or
        row >= len(game_world.player.tools)):
        return -1
    return row

def calculate_blocks_index(row, col):
    if (row != 2 or
        col < 0 or
        col >= len(game_world.player.blocks)):
        return -1
    return col

def on_right_click(x,y):
    row, col = calculate_coordinates(x,y)
    position = calculate_grid_index(row, col)
    if position >= 0:
        if game_world.blocks[position].name == "Air":
            game_world.update_block(position, b.Block("Stone", 3,1, "grey"))
            game_world.draw_world(painter)


painter = painter.Painter()
turtle.tracer(0,0)

turtle.onscreenclick(on_click)
turtle.onscreenclick(on_right_click, 3)

game_world = gameworld.World(10,10)
game_world.generate_world()
game_world.draw_world(painter)
game_world.draw_player(painter)
turtle.update()

turtle.mainloop()
