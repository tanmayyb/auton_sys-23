from cgitb import text
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, scrolledtext

from threading import *

from settings.window import *
from settings.grid import *


class statusBar():
    def __init__(self, parent, window):
        self.window = window
        self.parent = parent

        self.show_status_bar()
    
    def show_status_bar(self):
        self.status_bar_frame = LabelFrame(
            self.window,
            text="Controller Connection/Status")
        self.status_bar_frame.grid(
                row=STATUS_BAR_FRAME_ROW, 
                column=STATUS_BAR_FRAME_COLUMN,
                rowspan=STATUS_BAR_FRAME_ROWSPAN,
                columnspan=STATUS_BAR_FRAME_COLUMNSPAN, 
                sticky=STATUS_BAR_FRAME_STICKY)

        self.controller_status = Label(
            self.status_bar_frame,
            text="Controller Status")
        
        self.controller_status.pack(
            padx=5, 
            pady=5,
            side=LEFT)

        self.controller_info = Label(
            self.status_bar_frame,
            text="\tInfo")
        
        self.controller_info.pack(
            padx=5, 
            pady=5,
            side=LEFT)

        self.teleop_speed_info = Label(
            self.status_bar_frame,
            text="Speed:\t \t")
        
        self.teleop_speed_info.pack(
            padx=5, 
            pady=5,
            side=RIGHT)


    def set_status_bar_controller_state(self, msg):
        self.controller_status.configure(text="Controller Status: "+msg)

    def set_status_bar_controller_info(self, msg):
        self.controller_info.configure(text="\tInfo: "+msg)

    def set_status_bar_speed_info(self, msg):
        self.teleop_speed_info.configure(text=f"Speed:\t{10.0*float(msg):.1f}\t")