from tkinter import *
from tkinter.ttk import *
from tkinter import PhotoImage, StringVar, Label, scrolledtext
from threading import *
import time

from base_station import baseNode

from window import WIN_WIDTH, WIN_HEIGHT, WIN_X_POSITION, SETUP_STRING

import rclpy

from rclpy.executors import MultiThreadedExecutor


class gui(Thread):

    def __init__(self, window):
        Thread.__init__(self)
        """
        0 1 2 3 4 respectively
        """
        self.state_array = ["Initializing","Standby/Idle","Moving","Manual"] 
        self.state = None

        self.window = window
        self.draw_gui()
        self.setup_window()



        rclpy.init(args=None)
        
        self.setup_nodes()
        
        print("gui initialised")

    def fetch_state(self, state):
        self.state = self.state_array[state]

    def setup_window(self):
         # Window setup
        self.window.title("Auton ROS GUI")
        self.window.geometry(SETUP_STRING)
        # GUI Styles
        self.style = Style(self.window)
        self.style.configure('Info.TLabel',
                             font=('Arial', 12),
                             background='#C2C1C2',
                             anchor='center')
        
    def setup_nodes(self):

        self.base_node = baseNode(self)

        """
        Threading
        """
        self.executor = MultiThreadedExecutor()
        self.executor.add_node(self.base_node)
        self.executor_thread = Thread(
            target=self.executor.spin, 
            daemon=True)
        self.executor_thread.start()


    
    def fetch_result(self, num):
        print("I got Called, I got:", num)

    def display_action_feedback(self, caller, msg):
        self.action_scroll.insert(
            END,
            f"[ {str(caller)} ]: {str(msg)}"+'\n')
        self.action_scroll.see('end')
        
    def button1(self):
        self.base_node.do_pub(2)    #fix message type

    def a_button_1(self):
        self.base_node.send_goal(10)
        
    def show_buttons(self):
        #button pub sub buttons
        self.pub_button = Button(
            self.window, 
            text="Send Pub", 
            style="button.TButton", 
            command=self.button1).grid(
                row=7, 
                column=0, 
                columnspan=3)
        
        #action service buttons
        self.action_button = Button(
            self.window, 
            text="Do Action", 
            style="button.TButton", 
            command=self.a_button_1).grid(
                row=10, 
                column=0, 
                columnspan=3)
    
    
    def show_scroll(self):
        self.scroll = scrolledtext.ScrolledText(
            self.window, 
            height=8, 
            width=32, 
            font=('Arial 14'), 
            borderwidth=0,)

        self.scroll.grid(
                row=0, 
                column=0, 
                columnspan=3, 
                rowspan=2, 
                pady=(10, 0))
        
        self.action_scroll = scrolledtext.ScrolledText(
            self.window, 
            height=8, 
            width=32, 
            font=('Arial 14'), 
            borderwidth=0,)
        
        self.action_scroll.grid(
                row=2, 
                column=0, 
                columnspan=3, 
                rowspan=2, 
                pady=(10, 0))

    def insert_in_scroll(self, data):
        data = str(data)
        self.scroll.insert(END,"rec:   "+data+'\n')
        self.scroll.see('end')

    def draw_gui(self):
        
        self.show_scroll()
        self.show_buttons()
    