from cgitb import text
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, scrolledtext

from settings.window import *
from settings.grid import *

class scroll():
    def __init__(self, parent, window):
        self.window = window
        self.parent = parent

        self.show_scroll()
    
    def show_scroll(self):
        
        self.scroll_frame = LabelFrame(
            self.window, 
            text="feed")
        
        self.scroll_frame.grid(
                row=SCROLL_FRAME_ROW, 
                column=SCROLL_FRAME_COLUMN,
                rowspan=SCROLL_FRAME_ROWSPAN,
                columnspan=SCROLL_FRAME_COLUMNSPAN)
        
        self.event_scroll = scrolledtext.ScrolledText(
            self.scroll_frame, 
            height=10, 
            width=40, 
            font=('Arial 12'), 
            borderwidth=0,)
        
        self.event_scroll.pack(
            padx=5, 
            pady=5)

        self.feedback_scroll = scrolledtext.ScrolledText(
            self.scroll_frame, 
            height=10, 
            width=40, 
            font=('Arial 12'), 
            borderwidth=0,)
        self.feedback_scroll.pack(
            padx=5, 
            pady=5)

    """DISPLAY FUNCTIONS FOR TEXT FIELDS """
    def display_action_feedback(self, caller, msg, show_type=TRUE):
        id = None
        
        if caller == "miniwalk_feedback":
            if show_type == 1:
                id = "[mW_feedback]"
            
            d2t = str(msg.d2t)[:6]
            he = str(msg.he)[:6]
            
            self.feedback_scroll.insert(
                END,
                f"{id}:     d2t: {d2t}     he: {he}"+'\n')
            self.feedback_scroll.see('end')

    def print_result(self, caller, result):
        print(f"{caller}", result)

    def insert_in_scroll(self, data):
        data = str(data)
        self.event_scroll.insert(END,"rec:   "+data+'\n')
        self.event_scroll.see('end')