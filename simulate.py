import numpy as np
from models import Cell, Landscape

FOREST_SPEED = 10 
GRASS_SPEED = 25    # https://www.cfa.vic.gov.au/plan-prepare/grassfires-rural
FIRE_JUMP_CHANCE = 0.002

DX = [1, 1, 0, -1, -1, -1, 0, 1]
DY = [0, 1, 1, 1, 0, -1, -1, -1]

def loop():

    for y in range(landscape.rows):
        for x in range(landscape.cols):
            cell = landscape.grid[y][x]

            if cell.state == Cell.FIRE_STATE and cell.check_burn():
                landscape.update_cell(x, y, fire = False, state = Cell.ASH_STATE)
            elif cell.state == Cell.FOREST_STATE or cell.state == Cell.GRASS_STATE:
                pass

if __name__ == "__main__":
    landscape = Landscape()


