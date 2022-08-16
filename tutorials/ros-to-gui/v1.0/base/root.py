from tkinter import *

def root_():
    root = Tk()
    n_rows = 15
    n_columns = 5
    # Configure number of grids in each row and column in gui
    for i in range(n_rows):
        root.grid_rowconfigure(i, weight=1)
    for i in range(n_columns):
        root.grid_columnconfigure(i, weight=1)
    return root