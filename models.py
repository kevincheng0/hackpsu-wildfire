import numpy as np

class Cell:
    EMPTY_STATE = 0
    FOREST_STATE = 1
    GRASS_STATE = 2
    WATER_STATE = 3
    ASH_STATE = 4
    FOREST_BURN_TIME = 0.8
    GRASS_BURN_TIME = 0.1

    def __init__(self, x, y, size, state, fire):
        self.x = x
        self.y = y
        self.size = size
        self.state = state
        self.elevation = elevation
        self.fire = fire

    def update_state(self, new_state):
        self.state = new_state
    
    def update_elevation(self, new_elevation):
        self.elevation = new_elevation
    
    def update_fire(self):
        self.fire = not self.fire

    def check_burn(self):
        if self.state == Cell.FOREST_STATE and np.random.random() > Cell.FOREST_BURN_TIME:
            return True
        elif np.random.random() > Cell.GRASS_BURN_TIME:
            return True
        else:
            return False

class Landscape:

    def __init__(self, rows, cols, cell_size, wind):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[Cell(x, y, cell_size, Cell.EMPTY_STATE, False) for x in range(cols)] for y in range(rows)]
        self.wind = wind    # radians

    def update_cell(self, x, y, new_state = None, new_elevation = None, fire = False):
        if new_state:
            self.grid[y][x].update_state(new_state)
        
        if new_elevation:
            self.grid[y][x].update_elevation(new_elevation)

        if fire:
            self.grid[y][x].update_fire()

    def update_wind(self, new_wind):
        self.wind = wind

    # get some better values
    def wind_weight(self, wind, direction):
        angle = np.arctan(direction[0] / direction[1])
        if wind:
            return (np.cos(wind - angle)**2 + 0.2) / 1.3
        else:
            return 0.5