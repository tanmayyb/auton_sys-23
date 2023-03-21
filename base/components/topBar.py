from tkinter import *
from tkinter.ttk import *

from threading import *

from test2 import *

class topBar():
    def __init__(self, window):
        self.window = window

        self.show_top_bar()

    def feature_button_action(self):
        self.paramFeature_BT.configure(state=DISABLED)
        launchFWindow(self.window)
        self.paramFeature_BT.configure(state=NORMAL)

    def show_top_bar(self):
        self.top_frame = Frame(self.window, width=800, height = 40, borderwidth=1, relief=GROOVE)
        self.top_frame.grid(row=0, 
                column=0,
                columnspan=5,
                sticky="NW")

        self.top_frame.propagate(FALSE)
                
        self.paramFeature_BT = Button(
            self.top_frame, 
            text="Feature",
            command = lambda: Thread(target=self.feature_button_action, daemon=True).start()
            )
        self.paramFeature_BT.pack(side=RIGHT, padx=5, pady=5)

        self.status_led_rover = Canvas(self.top_frame, width=30)
        self.status_led_rover.create_oval(9,9,26,26)
        self.status_led_rover.pack(side=LEFT)

        self.status_led_rover_label = Label(self.top_frame, text="Rover")
        self.status_led_rover_label.pack(side=LEFT)

        self.status_led_node2 = Canvas(self.top_frame, width=30)
        self.status_led_node2.create_oval(9,9,26,26)
        self.status_led_node2.pack(side=LEFT)

        self.status_led_node2_label = Label(self.top_frame, text="Node2")
        self.status_led_node2_label.pack(side=LEFT)

        self.status_led_node3 = Canvas(self.top_frame, width=30)
        self.status_led_node3.create_oval(9,9,26,26)
        self.status_led_node3.pack(side=LEFT)

        self.status_led_node3_label = Label(self.top_frame, text="Node3")
        self.status_led_node3_label.pack(side=LEFT)

        self.status_led_node4 = Canvas(self.top_frame, width=30)
        self.status_led_node4.create_oval(9,9,26,26)
        self.status_led_node4.pack(side=LEFT)

        self.status_led_node4_label = Label(self.top_frame, text="Node4")
        self.status_led_node4_label.pack(side=LEFT)

        self.status_led_node5 = Canvas(self.top_frame, width=30)
        self.status_led_node5.create_oval(9,9,26,26)
        self.status_led_node5.pack(side=LEFT)

        self.status_led_node5_label = Label(self.top_frame, text="Node5")
        self.status_led_node5_label.pack(side=LEFT)


