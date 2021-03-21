from tkinter import *
import numpy as np

class Cell():
    EMPTY_COLOR_BG = "white"
    EMPTY_COLOR_BORDER = "white"
    FILLED_COLOR_BG = "green"
    FILLED_COLOR_BORDER = "green"
    FIRE_COLOR_BG = "red"
    FIRE_COLOR_BORDER = "red"
    EMPTY_STATE = 0
    FOREST_STATE = 1
    FIRE_STATE = 2

    def __init__(self, master, x, y, size, state = EMPTY_STATE, fill = False):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size = size
        self.fill = fill
        self.state = state

    def _switch(self, all_trees = False):
        """ reverses fill and sets state to the opposite (1, 2 -> 0). Exception for all trees function. """
        if all_trees:
            self.fill = True
            self.state = Cell.FOREST_STATE
        else:
            self.fill = not self.fill
            self.state = not self.state

    def draw(self):
        """ requires cell to switch fill first. Only applies to switching anything to empty and empty to tree """
        if self.master != None :
            fill = Cell.FILLED_COLOR_BG
            outline = Cell.FILLED_COLOR_BORDER

            if not self.fill:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline, tag = "cell")

    def light_fire(self):
        """ sets filled to true and state to FIRE_STATE, and changes the color """
        if self.master != None:
            fill_colour = Cell.FIRE_COLOR_BG
            outline_colour = Cell.FIRE_COLOR_BORDER
            self.fill = True
            self.state = Cell.FIRE_STATE

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill_colour, outline = outline_colour, tag = "cell")

class CellGrid(Canvas):
    FOREST_FRACTION = 2
    BRUSH_ADD_TREE = "add_tree"
    BRUSH_REMOVE_TREE = "remove_tree"
    BRUSH_ADD_FIRE = "add_fire"
    BRUSH_DEBUG = "debug"

    def __init__(self,master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        self.winfo_toplevel().title("Basic Fire Model")
        self.cellSize = cellSize
        self.rows = rowNumber
        self.cols = columnNumber
        self.brush = CellGrid.BRUSH_ADD_TREE

        self.grid = [[0 for x in range(self.cols)] for y in range(self.rows)]
        self.init_grid()

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []

        #bind click action
        self.bind("<Button-1>", self.handleMouseClick)  
        #bind moving while clicking
        self.bind("<B1-Motion>", self.handleMouseMotion)
        #bind release button action - clear the memory of midified cells.
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.draw()

    def init_grid(self, trees = True):
        for y in range(self.rows):
            for x in range(self.cols):
                is_forest = np.random.random() < CellGrid.FOREST_FRACTION and trees
                self.grid[y][x] = (Cell(self, x, y, self.cellSize, fill = is_forest, state = is_forest))
                
                if is_forest:
                    self.grid[y][x].draw()

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if self.brush == CellGrid.BRUSH_DEBUG:
            print(f"fill: {cell.fill}, state: {cell.state}")

        if self.brush == CellGrid.BRUSH_ADD_FIRE:
            #print("lighting fire")
            cell.light_fire()

        if cell not in self.switched and (not cell.fill and self.brush == CellGrid.BRUSH_ADD_TREE) or (cell.fill and self.brush == CellGrid.BRUSH_REMOVE_TREE):
            #print("drawing")
            cell._switch()
            cell.draw()
            
        self.switched.append(cell)         # add the cell to the list of cell switched during the click
 

    def handleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if self.brush == CellGrid.BRUSH_ADD_FIRE:
            #print("lighting fire")
            cell.light_fire()

        if cell not in self.switched and (not cell.fill and self.brush == CellGrid.BRUSH_ADD_TREE) or (cell.fill and self.brush == CellGrid.BRUSH_REMOVE_TREE):
            #print("drawing")
            cell._switch()
            cell.draw()
            
        self.switched.append(cell)


    def add_tree(self):
        self.brush = CellGrid.BRUSH_ADD_TREE

    def remove_tree(self):
        self.brush = CellGrid.BRUSH_REMOVE_TREE

    def add_fire(self):
        self.brush = CellGrid.BRUSH_ADD_FIRE

    def all_tree(self):
        for y in range(self.rows):
            for x in range (self.cols):
                cell = self.grid[y][x]
                #print(cell.state)
                if cell.state != Cell.FOREST_STATE:
                    #print("filling")
                    cell._switch(all_trees = True)
                    cell.draw()

    def clear_all(self):
        print("deleting all cells")
        self.delete("cell")
        self.init_grid(trees = False)

    def debug(self):
        self.brush = CellGrid.BRUSH_DEBUG