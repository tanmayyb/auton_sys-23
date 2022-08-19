from tkinter import *
from tkinter.ttk import *
from tkinter import Label, scrolledtext

import tkintermapview
from threading import *
import time

from base import baseNode

from window import *

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
        
        self.setup_window()
        self.draw_gui()

        rclpy.init(args=None)
        
        self.setup_nodes()
        
        print("gui initialised")

    def fetch_state(self, state):
        self.state = self.state_array[state]

    def setup_window(self):
         # Window setup
        self.window.title("Auton ROS GUI")
        self.window.geometry(SETUP_STRING)
        self.setup_styles()

    def setup_styles(self):
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

    def show_map(self):
        
        self.map_frame = LabelFrame(
            self.window,
            text="map")
        self.map_frame.grid(
                row=0, 
                column=0,
                rowspan=5,
                columnspan=5)

        self.map_widget = tkintermapview.TkinterMapView(
            self.map_frame, 
            width=400, 
            height=400, 
            corner_radius=0)

        self.map_widget.grid(
            row=0,
            column=0)

        # set current widget position and zoom
        self.map_widget.set_position(
            43.65897373429778, 
            -79.37932931217927)  # Ryerson
        self.map_widget.set_marker(
            43.65897373429778, 
            -79.37932931217927, 
            text="Ryerson Uni")
        self.map_widget.set_zoom(20)
    
    
        
    def button1(self):
        self.base_node.do_pub()    #fix message type

    def a_button_1(self):
        self.base_node.send_goal(10)

    def a_button_2(self):
        self.base_node.send_minimal_walk_goal(10.0,12.5)
    
    def a_button_3(self):
         self.base_node.send_minimal_walk_goal(10.0,12.5)

        
    def show_buttons(self):
        #button pub sub buttons
        
        self.button_label_frame = LabelFrame(self.window)

        self.button_label_frame.grid(
                row=7, 
                column=5,
                rowspan=3,
                columnspan=4)

        self.pub_button = Button(
            self.button_label_frame, 
            text="Send Simple Pub", 
            command=self.button1).pack()
            # .grid(
            #     row=7, 
            #     column=5, 
            #     columnspan=3)
        
        #action service buttons
        self.action_button = Button(
            self.button_label_frame, 
            text="Do Fibo Action",  
            command=self.a_button_1).pack()
            # .grid(
            #     row=10, 
            #     column=5, 
            #     columnspan=3)
        self.action_button_2 = Button(
            self.button_label_frame, 
            text="Do Custom Action",  
            command=self.a_button_2).pack()

        self.cancel_action_button = Button(
            self.button_label_frame, 
            text="Cancel Custom Action",  
            command=self.a_button_1).pack()
            # .grid(
            #     row=10, 
            #     column=5, 
            #     columnspan=3)
    
    def show_scroll(self):
        
        self.scroll_frame = LabelFrame(
            self.window, 
            text="scrolls")
        
        self.scroll_frame.grid(
                row=0, 
                column=5,
                rowspan=2,
                columnspan=3)
        
        self.event_scroll = scrolledtext.ScrolledText(
            self.scroll_frame, 
            height=8, 
            width=32, 
            font=('Arial 14'), 
            borderwidth=0,)
        
        self.event_scroll.pack(
            padx=5, 
            pady=5)
        # self.scroll.grid(
        #         row=0, 
        #         column=8, 
        #         columnspan=3, 
        #         rowspan=2, 
        #         pady=(10, 0))
        
        self.feedback_scroll = scrolledtext.ScrolledText(
            self.scroll_frame, 
            height=8, 
            width=32, 
            font=('Arial 14'), 
            borderwidth=0,)
        self.feedback_scroll.pack(
            padx=5, 
            pady=5)
        
        # self.action_scroll.grid(
        #         row=3, 
        #         column=8, 
        #         columnspan=3, 
        #         rowspan=2, 
        #         pady=(10, 0))

    def fetch_result(self, caller, result):
        print(f"{caller}", result)

    def display_action_feedback(self, caller, msg):
        self.action_scroll.insert(
            END,
            f"[ {str(caller)} ]: {str(msg)}"+'\n')
        self.action_scroll.see('end')

    def insert_in_scroll(self, data):
        data = str(data)
        self.scroll.insert(END,"rec:   "+data+'\n')
        self.scroll.see('end')

    def draw_gui(self):
        self.show_map()
        
        self.show_scroll()
        self.show_buttons()
    