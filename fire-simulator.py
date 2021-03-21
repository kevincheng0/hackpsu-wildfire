from tkinter import *
import numpy as np
import time
from models import Cell, CellGrid



NY = ([-1,-1,-1,0,0,1,1,1])
NX = ([-1,0,1,-1,1,-1,0,1])
NZ=([.13,.13,.13,.13,.9,.13,.9,.9])

def run_app():
    #print("looping")

    for y in range(frm_grid.rows):
        for x in range(frm_grid.cols):
            cell = frm_grid.grid[y][x]

            #TODO: Add fuel state, elevation, water, object deletion, shift wind
            if cell.state == Cell.FIRE_STATE:
                cell._switch()
                cell.draw()

            elif cell.state == Cell.FOREST_STATE:

                for i in range(0, 7):
                    new_y = y + NY[i]
                    new_x = x + NX[i]
                    if new_y < 0 or new_y >= frm_grid.cols or new_x < 0 or new_x >= frm_grid.rows:
                        continue
                    if frm_grid.grid[new_y][new_x].state == Cell.FIRE_STATE and np.random.random() <= NZ[i]:
                        cell.light_fire()
                        break

                if np.random.random() <= 0.000001:
                    cell.light_fire()


    root.after(500, run_app)

if __name__ == "__main__":
    root = Tk()
    cols = 50
    rows = 50
    print(rows, cols)

    frm_grid = CellGrid(root, rows, cols, 10, bg = "snow")
    frm_grid.pack()

    frm_ui = Frame(bg = "LightSteelBlue3", width = cols * 10, relief = "raised")
    frm_ui.pack(fill = "both", side = "bottom")

    btn_run = Button(frm_ui, command = run_app, text = "Start", width = 10, height = 2)
    btn_run.pack(side = "left", padx = 10, pady = 5)

    btn_add_tree = Button(frm_ui, command = frm_grid.add_tree, text = "Add\nTrees", width = 10, height = 2)
    btn_add_tree.pack(side = "left", padx = 10, pady = 5)

    btn_remove_tree = Button(frm_ui, command = frm_grid.remove_tree, text = "Erase\nTrees", width = 10, height = 2)
    btn_remove_tree.pack(side = "left", padx = 10, pady = 5)
    
    btn_all_tree = Button(frm_ui, command = frm_grid.all_tree, text = "All\nTrees", width = 10, height = 2)
    btn_all_tree.pack(side = "left", padx = 10, pady = 5)

    btn_no_tree = Button(frm_ui, command = frm_grid.clear_all, text = "Clear\nAll", width = 10, height = 2)
    btn_no_tree.pack(side = "left", padx = 10, pady = 5)

    btn_lighter = Button(frm_ui, command = frm_grid.add_fire, text = "Lighter", width = 10, height = 2)
    btn_lighter.pack(side = "left", padx = 10, pady = 5)

    #btn_debug = Button(frm_ui, command = frm_grid.debug, text = "Debug", width = 10, height = 2)
    #btn_debug.pack(side = "left", padx = 10, pady = 5)
    
    btn_stop = Button(frm_ui, command = quit, text = "Stop", width = 10, height = 2)
    btn_stop.pack(side = "left", padx = 10, pady = 5)

    root.mainloop()

