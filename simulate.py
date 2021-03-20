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
            random = np.random.random() * 25

            if cell.state == Cell.FIRE_STATE and cell.check_burn():
                landscape.update_cell(x, y, fire = False, state = Cell.ASH_STATE)
                # colour change
            elif cell.state == Cell.FOREST_STATE and random < FOREST_SPEED or cell.state == Cell.GRASS_STATE and random < GRASS_SPEED:
                for i in range(7):
                    new_y = y + DY[i]
                    new_x = x + DX[i]
                    if new_x < 0 or new_y < 0 or new_x >= landscape.cols or new_y >= landscape.cols:
                        break
                    elif landscape.grid[new_y][new_x] == Cell.FIRE_STATE and np.random.random() <= Landscape.wind_weight(DX[i], DY[i]):
                        landscape.update_cell(x, y, fire = True)
                        # colour change

def clear():
    landscape.init_grid()

if __name__ == "__main__":
    landscape = Landscape(100, 100, 10, 0)
    

