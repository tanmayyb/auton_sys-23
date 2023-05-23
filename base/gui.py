from cgitb import text
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, scrolledtext

from threading import *

from nodes.base import baseNode

from settings.window import *
from settings.grid import *

from components.topBar import *
from components.map import *
from components.statusBar import *
from components.scroll import *
from components.actionConsole import *

import rclpy

from rclpy.executors import MultiThreadedExecutor
from plugins.teleop.teleop import teleop_processor


class gui(Thread):
    def __init__(self, window):
        Thread.__init__(self)

        self.window = window

        self.state_array = ['IDLE/STANDBY', 'MINIWALKING','', 'TELEOP']

        self.setup_window()
        self.draw_gui()

        rclpy.init(args=None)
        
        self.setup_nodes()
        
        print("gui initialized")

    def fetch_state(self, state):
        self.state = self.state_array[state]
    
    def setup_window(self):
         # Window setup
        self.window.title("auton_sys-23 mission gui")
        self.window.geometry(SETUP_STRING)
        #self.window.minsize(WIN_WIDTH, WIN_HEIGHT)
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

        self.teleop = teleop_processor(self)
        self.teleop.daemon = True
        self.teleop.start()
    
    def draw_gui(self):
        self.topBar = topBar(self, self.window)

        self.map = map(self, self.window)

        self.statusBar = statusBar(self, self.window)

        self.actionConsole = actionConsole(self, self.window)

        self.scroll = scroll(self, self.window)

