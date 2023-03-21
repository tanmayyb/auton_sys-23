from tkinter import *
from tkinter.ttk import *

from threading import *

from topBar import *

from map import *

class test():
    def __init__(self, window):
        self.window = window

        app = topBar(self.window)

        app2 = map(self.window)

    


if __name__ == '__main__':
    window = Tk()
    app = test(window)
    window.mainloop()