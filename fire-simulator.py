from tkinter import *
import numpy as np
from models import Cell, CellGrid


NY = ([0, 1, 1, 1, 0, -1, -1, -1])
NX = ([1, 1, 0, -1, -1, -1, 0, 1])

def run_app():
    #print("looping")

    for y in range(frm_grid.rows):
        for x in range(frm_grid.cols):
            cell = frm_grid.grid[y][x]

            if cell.state == Cell.FIRE_STATE:
                adj_trees = 0
                for i in range(0, 7):
                    new_y = y + NY[i]
                    new_x = x + NX[i]
                    if new_y < 0 or new_y >= frm_grid.cols or new_x < 0 or new_x >= frm_grid.rows:
                        continue
                    else:
                        if frm_grid.grid[new_y][new_x].state == Cell.FOREST_STATE:
                            adj_trees += 1

                if np.random.random() <= 0.2 or adj_trees == 0:
                    cell._switch()
                    cell.draw()
                else:
                    cell.update_fire()

            if cell.state == Cell.FOREST_STATE:

                for i in range(0, 7):
                    new_y = y + CellGrid.NY[i]
                    new_x = x + CellGrid.NX[i]
                    if new_y < 0 or new_y >= frm_grid.cols or new_x < 0 or new_x >= frm_grid.rows:
                        continue
                        
                    adj_cell = frm_grid.grid[new_y][new_x]
                    if adj_cell.state == Cell.FIRE_STATE and adj_cell.old_fire and np.random.random() <= frm_grid.wind[i]:
                        cell.light_fire()
                        break

                if np.random.random() <= 0.000001:
                    cell.light_fire()


    root.after(500, run_app)

if __name__ == "__main__":
    root = Tk()
    cols = 100
    rows = 100
    #print(rows, cols)

    root.configure(background="PeachPuff3")

    frm_grid = CellGrid(root, rows, cols, 5, bg = "snow")
    frm_grid.pack()

    frm_ui = Frame(bg = "PeachPuff4", width = cols * 10, relief = "raised")
    frm_ui.pack(fill = "both", side = "bottom")

    frm_ui_2 = Frame(bg = "PeachPuff4", width = cols * 10, relief = "raised")
    frm_ui_2.pack(side = "bottom")

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

    btn_no_wind = Button(frm_ui_2, command = frm_grid.no_wind, text = "Wind: None", width = 10, height = 1)
    btn_no_wind.pack(side = "left", padx = 10, pady = 5)

    btn_wind_N = Button(frm_ui_2, command = frm_grid.wind_N, text = "Wind: N", width = 10, height = 1)
    btn_wind_N.pack(side = "left", padx = 10, pady = 5)

    btn_wind_E = Button(frm_ui_2, command = frm_grid.wind_E, text = "Wind: E", width = 10, height = 1)
    btn_wind_E.pack(side = "left", padx = 10, pady = 5)

    btn_wind_S = Button(frm_ui_2, command = frm_grid.wind_S, text = "Wind: S", width = 10, height = 1)
    btn_wind_S.pack(side = "left", padx = 10, pady = 5)

    btn_wind_W = Button(frm_ui_2, command = frm_grid.wind_W, text = "Wind: W", width = 10, height = 1)
    btn_wind_W.pack(side = "left", padx = 10, pady = 5)



    root.mainloop()

