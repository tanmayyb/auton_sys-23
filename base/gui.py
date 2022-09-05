from tkinter import *
#import tkinter as tk # for textfields
from tkinter.ttk import *
from tkinter import Label, scrolledtext
from turtle import width

import tkintermapview
from threading import *
import time

from base import baseNode

from window import *

import rclpy

from rclpy.executors import MultiThreadedExecutor
from plugins.teleop.teleop import teleop_processor


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
    
    def show_text_fields(self):

        self.text_field_label_frame = LabelFrame(self.window)
        self.text_field_label_frame.grid(
                row=7, 
                column=2,
                rowspan=3,
                columnspan=7, 
                sticky="W")

        self.text_field_labels = LabelFrame(self.text_field_label_frame)
        self.text_field_label_frame_text_fields = LabelFrame(self.text_field_label_frame)


        """TEXT FIELD LABELS"""
        self.text_field_labels.grid(
                row=0, 
                column=0)

        self.input_geofence_label = Label(
            self.text_field_labels, 
            text="Input Geofence")
        self.input_geofence_label.pack(
            padx=5,
            pady=5)

        self.input_tlat_label = Label(
            self.text_field_labels, 
            text="Input Target Lat")
        self.input_tlat_label.pack(
            padx=5,
            pady=5)


        self.input_tlat_label = Label(
            self.text_field_labels, 
            text="Input Target Lon")
        self.input_tlat_label.pack(
            padx=5,
            pady=5)


        """TEXT FIELDS"""
        self.text_field_label_frame_text_fields.grid(
                row=0, 
                column=1)

        self.input_geofence = StringVar()
        self.input_geofence_textbox = Entry(
            self.text_field_label_frame_text_fields, 
            textvariable=self.input_geofence)
        self.input_geofence_textbox.pack(
            padx=5,
            pady=5)

        self.input_tlat = StringVar()
        self.input_tlat_textbox = Entry(
            self.text_field_label_frame_text_fields, 
            textvariable=self.input_tlat)
        self.input_tlat_textbox.pack(
            padx=5,
            pady=5)

        self.input_tlon = StringVar()
        self.input_tlon_textbox = Entry(
            self.text_field_label_frame_text_fields, 
            textvariable=self.input_tlon)
        self.input_tlon_textbox.pack(
            padx=5,
            pady=5)

        self.input_geofence.set("2.0")
        self.input_tlat.set("43.6587021")
        self.input_tlon.set("-79.3792810")

        #KWAD CENTER
        #43.6587021
        #-79.3792810
        
    def simple_pub_button_1(self):
        self.base_node.do_pub()    #fix message type

    def action_button_1(self):
        self.base_node.send_goal(10)

    def action_button_2(self):
        self.base_node.send_goal_miniwalk(
            float(self.input_tlat.get()),
            float(self.input_tlon.get()))
    
    def cancel_action_button_1(self):
        self.base_node.cancel_miniwalk_goal()
        
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
            command=self.simple_pub_button_1).pack()
            
        #action service buttons
        self.action_button = Button(
            self.button_label_frame, 
            text="Do Teleop",  
            command=self.action_button_1).pack()

        self.action_button_2 = Button(
            self.button_label_frame, 
            text="Do MiniWalk",  
            command=self.action_button_2).pack()

        self.cancel_action_button = Button(
            self.button_label_frame, 
            text="Cancel MiniWalk",  
            command=self.cancel_action_button_1).pack()
    
    def show_scroll(self):
        
        self.scroll_frame = LabelFrame(
            self.window, 
            text="feed")
        
        self.scroll_frame.grid(
                row=0, 
                column=5,
                rowspan=2,
                columnspan=3)
        
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

    def fetch_result(self, caller, result):
        print(f"{caller}", result)

    def display_action_feedback(self, caller, msg, show_type=TRUE):
        id = None
        
        if caller == "miniwalk_feedback":
            if show_type == b'I01\n':
                id = "[feedback]"
            
            d2t = str(msg.d2t)[:6]
            he = str(msg.he)[:6]
            
            self.feedback_scroll.insert(
                END,
                f"{id}:    {d2t}     {he}"+'\n')
            self.feedback_scroll.see('end')

    def insert_in_scroll(self, data):
        data = str(data)
        self.event_scroll.insert(END,"rec:   "+data+'\n')
        self.event_scroll.see('end')

    def draw_gui(self):
        self.show_map()
        
        self.show_scroll()

        self.show_text_fields()
        self.show_buttons()
    