from cgitb import text
from tkinter import *
from tkinter.ttk import *
from tkinter import Label

from settings.window import *
from settings.grid import *

class topBar():
    def __init__(self, parent, window):
        self.window = window
        self.parent = parent

        self.show_top_bar()
        self.show_state()


    def show_top_bar(self):
        self.top_frame = Frame(self.window, width=WIN_WIDTH, height = 40, borderwidth=1, relief=GROOVE)
        self.top_frame.grid(row=0, 
                column=0,
                columnspan=5,
                sticky="NW")

        self.top_frame.propagate(FALSE)
                
        self.status_led_rover = Canvas(self.top_frame, width=30)
        self.rover_led = self.status_led_rover.create_oval(9,9,26,26)
        self.status_led_rover.pack(side=LEFT)

        self.status_led_rover_label = Label(self.top_frame, text="Rover")
        self.status_led_rover_label.pack(side=LEFT)


        self.status_led_node2 = Canvas(self.top_frame, width=30)
        self.sensors_led = self.status_led_node2.create_oval(9,9,26,26)
        self.status_led_node2.pack(side=LEFT)

        self.status_led_node2_label = Label(self.top_frame, text="Sensors")
        self.status_led_node2_label.pack(side=LEFT)


        self.status_led_node3 = Canvas(self.top_frame, width=30)
        self.teensy_led = self.status_led_node3.create_oval(9,9,26,26)
        self.status_led_node3.pack(side=LEFT)

        self.status_led_node3_label = Label(self.top_frame, text="Teensy")
        self.status_led_node3_label.pack(side=LEFT)


        self.status_led_node4 = Canvas(self.top_frame, width=30)
        self.cvs2_led = self.status_led_node4.create_oval(9,9,26,26)
        self.status_led_node4.pack(side=LEFT)

        self.status_led_node4_label = Label(self.top_frame, text="CVS2")
        self.status_led_node4_label.pack(side=LEFT)

        self.status_led_node5 = Canvas(self.top_frame, width=30)
        self.am_led = self.status_led_node5.create_oval(9,9,26,26)
        self.status_led_node5.pack(side=LEFT)

        self.status_led_node5_label = Label(self.top_frame, text="ActionM")
        self.status_led_node5_label.pack(side=LEFT)
       
        self.canvas_dic = {
           'rover_node': self.status_led_rover,
           'sensors_node': self.status_led_node2,
           'teensy_node': self.status_led_node3,
           'cv_subsystem_node': self.status_led_node4,
           'action_manager_node': self.status_led_node5
        }
        
        self.led_dic = {
           'rover_node': self.rover_led,
           'sensors_node': self.sensors_led,
           'teensy_node': self.teensy_led,
           'cv_subsystem_node': self.cvs2_led,
           'action_manager_node': self.am_led
        }

    def set_led_status(self, list):
        temp_list = ['rover_node', 'sensors_node', 'teensy_node', 'cv_subsystem_node', 'action_manager_node']
        for node in list:
            self.canvas_dic[node].itemconfig(self.led_dic[node], fill='#34eb58')
            temp_list.remove(node)

        for node in temp_list:
            self.canvas_dic[node].itemconfig(self.led_dic[node], fill='')

    def show_state(self):
        self.current_state = Label(self.top_frame, text= " ")
        self.current_state.pack(side=RIGHT, padx=5)
        
        self.state_label = Label(self.top_frame, text="Rover State:")
        self.state_label.pack(side=RIGHT)

    def set_state(self, state):
        self.current_state.config(text=state)
        
        
