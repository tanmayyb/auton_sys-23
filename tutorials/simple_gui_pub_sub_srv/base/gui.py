from tkinter import *
from tkinter.ttk import *
from tkinter import PhotoImage, StringVar, Label, scrolledtext
from threading import *
import time

from publisher import miniPub

from window import WIN_WIDTH, WIN_HEIGHT, WIN_X_POSITION, SETUP_STRING

import rclpy

from rclpy.executors import MultiThreadedExecutor


class gui(Thread):

    def __init__(self, window):
        Thread.__init__(self)

        self.window = window
        self.draw_gui(window)
        self.setup_window()



        rclpy.init(args=None)
        
        self.setup_nodes()
        
        print("gui initialised")

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
        
        #make nodes iterable
        #self.node_list = [miniPub,]

                # self.req_thread = Thread(
        #     target=rclpy.spin, 
        #     args=self.miniReq,
        #     daemon=True)
        # self.req_thread.start()  
        

        self.miniPub = miniPub(self)

        self.executor = MultiThreadedExecutor()
        self.executor.add_node(self.miniPub)
        # self.executor.add_node(self.miniReq)

        self.executor_thread = Thread(
            target=self.executor.spin, 
            daemon=True)
        self.executor_thread.start()


    
    def fetch_result(self, num):
        print("I got Called, I got:", num)
        
    def button1(self):
        self.miniPub.do_pub(2)    

    def button2(self):
        #self.miniReq.send_request(2,2)
        pass
    
    def show_buttons(self):
        #button for getting result from service
        self.pub_button = Button(
            self.window, 
            text="Send Pub", 
            style="button.TButton", 
            command=self.button1).grid(
                row=7, 
                column=0, 
                columnspan=3)
        

        self.action_button = Button(
            self.window, 
            text="Do Action", 
            style="button.TButton", 
            command=self.button2).grid(
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
        
        #self.scroll.pack()

    def insert_in_scroll(self, data):
        data = str(data)
        self.scroll.insert(END,"rec:   "+data+'\n')
        self.scroll.see('end')

    def draw_gui(self, window):
        
        self.show_scroll()
        self.show_buttons()
    