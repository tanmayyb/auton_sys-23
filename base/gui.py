from cgitb import text
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, scrolledtext

import tkintermapview
from threading import *
import time

from nodes.base import baseNode

from settings.window import *
from settings.grid import *

import rclpy

from rclpy.executors import MultiThreadedExecutor
from plugins.teleop.teleop import teleop_processor

import os


class gui(Thread):

    def __init__(self, window):
        Thread.__init__(self)
        
        
        self.state_array = ["Initializing","Standby/Idle","Moving","Manual"] 
        
        
        """ MAPS AND WAYPOINTS"""
        self.waypoints = 0
        self.markers = []
        self.path = None
        
        self.window = window
        
        self.home = (TMU_LAT, TMU_LON)

        self.setup_window()
        self.draw_gui()

        rclpy.init(args=None)
        
        self.setup_nodes()
        
        print("gui initialised")

    def fetch_state(self, state):
        self.state = self.state_array[state]

    def setup_window(self):
         # Window setup
        self.window.title("auton_sys-23 mission gui")
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

        self.teleop = teleop_processor(self)
        self.teleop.daemon = True
        self.teleop.start()



    def show_map(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        database_path = os.path.join(
            script_directory,
            "database", 
            "offline_tiles_tmu.db")

        self.map_frame = LabelFrame(
            self.window,
            text="map")
        self.map_frame.grid(
                row=MAP_FRAME_ROW, 
                column=MAP_FRAME_COLUMN,
                rowspan=MAP_FRAME_ROWSPAN,
                columnspan=MAP_FRAME_COLUMNSPAN)

        self.map_widget = tkintermapview.TkinterMapView(
            self.map_frame, 
            width=MAP_WIDTH, 
            height=MAP_HEIGHT, 
            corner_radius=MAP_CORNER_RADIUS,
            use_database_only=True,
            max_zoom=22,
            database_path=database_path)

        self.map_widget.grid(
            row=MAP_WIDGET_ROW,
            column=MAP_WIDGET_COLUMN,
            sticky = MAP_STICKY)

        # set current widget position and zoom
        self.map_widget.set_position(
            LAT_FOR_MAP, 
            LON_FOR_MAP)  # Ryerson
        self.rover_marker = self.map_widget.set_marker(
            LAT_FOR_MAP,
            LON_FOR_MAP, 
            text="Rover")

        self.map_widget.set_zoom(19)

        self.map_widget.add_right_click_menu_command(label="add waypoint",
                                                command=self.add_waypoint_on_map,
                                                pass_coords=True)
                                                
        self.map_widget.add_right_click_menu_command(label="pop last waypoint",
                                                command=self.pop_waypoints,
                                                pass_coords=False)

        self.map_widget.add_right_click_menu_command(label="go to coord",
                                                command=self.send_rover_to_point,
                                                pass_coords=True)


        self.map_widget.add_right_click_menu_command(label="load coordinates",
                                        command=self.load_coords,
                                        pass_coords=True)

        # self.map_widget.add_right_click_menu_command(label="go here",
        #                         command=self.load_coords,
        #                         pass_coords=True)

    def load_coords(self, coords):
        self.input_tlat.set(str(coords[0]))
        self.input_tlon.set(str(coords[1]))

        self.input_sw_tlat.set(str(coords[0]))
        self.input_sw_tlon.set(str(coords[1]))

    def send_rover_to_point(self, coords):


        if self.waypoints == 0:
            self.path = self.map_widget.set_path(
                [self.home,
                    (coords[0], coords[1])])
            
        if self.waypoints>0:
            self.path = self.map_widget.set_path(
                [self.markers[-1].position,
                (coords[0], coords[1])])
        
        self.waypoints = self.waypoints + 1
        new_marker = self.map_widget.set_marker(
            coords[0], 
            coords[1], 
            text="wp:"+str(self.waypoints))
        self.markers.append(new_marker)

        self.base_node.send_goal_miniwalk(
            float(coords[0]),
            float(coords[1]),
            float(self.input_geofence.get()))

    def add_waypoint_on_map(self, coords):
        self.waypoints = self.waypoints + 1
        new_marker = self.map_widget.set_marker(
            coords[0], 
            coords[1], 
            text="wp:"+str(self.waypoints))
        self.markers.append(new_marker)
        
        if self.waypoints==1:
            self.path = self.map_widget.set_path([self.home,self.markers[0].position])
        if self.waypoints>1:
            x = self.markers[self.waypoints-1].position[0]
            y = self.markers[self.waypoints-1].position[1]
            self.path.add_position(x,y)

            """ needed for updating path """
            self.path.add_position(x,y)
            self.path.remove_position(x,y)

    def pop_waypoints(self):
        x = self.markers[-1].position[0]
        y = self.markers[-1].position[1]
        
        if self.waypoints == 1:
            self.path.delete()
        if self.waypoints>1:
            self.path.remove_position(x,y)

        self.markers[-1].delete()
        self.markers.pop()
        self.waypoints= self.waypoints-1
        

    def show_action_console(self):

        self.input_tlat = StringVar()
        self.input_tlon = StringVar()
        self.input_geof = StringVar()

        self.input_geof.set("2.0")
        self.input_tlat.set("43.6587021")
        self.input_tlon.set("-79.3792810")

        # create a notebook
        self.actions_notebook = Notebook(self.window)
        self.actions_notebook.grid(
            row=ACTION_CONSOLE_FRAME_ROW, 
            column=ACTION_CONSOLE_FRAME_COLUMN,
            rowspan=ACTION_CONSOLE_FRAME_ROWSPAN,
            columnspan=ACTION_CONSOLE_FRAME_COLUMNSPAN,
            sticky=ACTION_CONSOLE_FRAME_STICKY)  

        # create frames for action consoles
        self.miniwalk_frame = Frame(self.actions_notebook, width=600, height=280)
        self.srch_act_frame = Frame(self.actions_notebook, width=600, height=280)

        self.draw_miniwalk_tab()
        self.draw_searchwalk_tab()
        



        #set frame placement
        self.miniwalk_frame.pack(fill='both', expand=True)
        self.srch_act_frame.pack(fill='both', expand=True)

        # add frames to notebook
        self.actions_notebook.add(self.miniwalk_frame, text='Miniwalk')
        self.actions_notebook.add(self.srch_act_frame, text='Searchwalk')



        #self.show_rover_info_labels(self.action_console_frame)

    def draw_miniwalk_tab(self):
        """
        frames of miniwalk tab
        """
        self.frame1_miniwalk_frame = LabelFrame(self.miniwalk_frame)
        self.frame2_miniwalk_frame = LabelFrame(self.miniwalk_frame)
        self.frame1_miniwalk_frame.grid(row=0,column=0)
        self.frame2_miniwalk_frame.grid(row=0,column=1)
        """
        elements of frame 1 of miniwalk
        """
        # labels 
        self.input_srad_label1 = Label(self.frame1_miniwalk_frame, text = "Input GeoF")
        self.input_tlat_label1 = Label(self.frame1_miniwalk_frame, text = "Input TLat")
        self.input_tlon_label1 = Label(self.frame1_miniwalk_frame, text = "Input TLon")
        self.input_srad_label1.grid(row=0,column=0)
        self.input_tlat_label1.grid(row=1,column=0)
        self.input_tlon_label1.grid(row=2,column=0)

        #text fields
        self.input_geof1 = Entry(self.frame1_miniwalk_frame,textvariable=self.input_geof)
        self.input_tlat1 = Entry(self.frame1_miniwalk_frame,textvariable=self.input_tlat)
        self.input_tlon1 = Entry(self.frame1_miniwalk_frame,textvariable=self.input_tlon)
        # adjust elements in grid
        self.input_geof1.grid(row=0,column=1,columnspan=4)
        self.input_tlat1.grid(row=1,column=1,columnspan=4)
        self.input_tlon1.grid(row=2,column=1,columnspan=4)

        """
        elements of frame 2 of miniwalk
        """
        self.do_miniwalk_bttn = Button(self.frame2_miniwalk_frame, text ="Do Miniwalk", command=self.do_miniwalk)
        self.cancel_miniwalk_bttn = Button(self.frame2_miniwalk_frame, text ="Cancel Miniwalk", command=self.stop_standby_button_3)
        # adjust elements in grid
        self.do_miniwalk_bttn.grid(row=0,column=0)
        self.cancel_miniwalk_bttn.grid(row=1,column=0)

        self.stop_button = Button(self.frame2_miniwalk_frame, text=" Stop/Standby", command=self.stop_standby_button_3)
        self.action_button = Button(self.frame2_miniwalk_frame, text="  Do Teleop  ",  command=self.do_teleop_button_4)

        self.stop_button.grid(row=0,column=1)
        self.action_button.grid(row=1,column=1)

    def do_miniwalk(self):
        tlat = float(self.input_tlat.get())
        tlon = float(self.input_tlon.get())
        geof = float(self.input_geof.get())
        print("sending minwalk goal to base node: ", tlat, tlon, geof)
        self.base_node.send_goal_miniwalk(tlat,tlon, geof)

    def draw_searchwalk_tab(self):
        """
        frames of search tab
        """
        # add elements in the search action frame
        self.frame1_srch_act_frame = LabelFrame(self.srch_act_frame) #left frame
        self.frame2_srch_act_frame = LabelFrame(self.srch_act_frame) #right frame
        # adjust frames in search action frame grid
        self.frame1_srch_act_frame.grid(row=0, column=0)
        self.frame2_srch_act_frame.grid(row=0, column=1)

        """
        elements of frame 1 of searchwalk
        """
        # labels 
        self.input_tlat_label2 = Label(self.frame1_srch_act_frame, text = "Input TLat")
        self.input_tlon_label2 = Label(self.frame1_srch_act_frame, text = "Input TLon")
        self.input_srad_label2 = Label(self.frame1_srch_act_frame, text = "Input SRad")
        self.input_tlat_label2.grid(row=0,column=0)
        self.input_tlon_label2.grid(row=1,column=0)
        self.input_srad_label2.grid(row=2,column=0)

        #text fields
        self.input_sw_tlat = StringVar()
        self.input_sw_tlon = StringVar()
        self.input_tlat2 = Entry(self.frame1_srch_act_frame, textvariable=self.input_sw_tlat)
        self.input_tlon2 = Entry(self.frame1_srch_act_frame, textvariable=self.input_sw_tlon)
        self.input_tlat2.grid(row=0,column=1,columnspan=4)
        self.input_tlon2.grid(row=1,column=1,columnspan=4)

        #radio buttons
        self.input_srad = DoubleVar()
        self.srad_radiobttn1 = Radiobutton(self.frame1_srch_act_frame, text="5m", variable=self.input_srad, value=5.0)
        self.srad_radiobttn2 = Radiobutton(self.frame1_srch_act_frame, text="10m", variable=self.input_srad, value=10.0)
        self.srad_radiobttn3 = Radiobutton(self.frame1_srch_act_frame, text="20m", variable=self.input_srad, value=20.0)
        self.srad_radiobttn1.grid(row=2,column=1)
        self.srad_radiobttn2.grid(row=2,column=2)
        self.srad_radiobttn3.grid(row=2,column=3)

        """
        elements of frame2 of searchwalk
        """
        self.enable_artag = IntVar()
        self.enable_obstacle_avoidance = IntVar()
        self.spattern = IntVar()

        self.artag_chkbttn = Checkbutton(self.frame2_srch_act_frame, text='enable_cv',variable=self.enable_artag, onvalue=1, offvalue=0)
        self.obstacle_avoidance_chkbttn = Checkbutton(self.frame2_srch_act_frame, text='enable_oa',variable=self.enable_obstacle_avoidance, onvalue=1, offvalue=0)
        # adjust elements in grid
        self.artag_chkbttn.grid(row=0,column=0)
        self.obstacle_avoidance_chkbttn.grid(row=1,column=0)

        self.spattern_radiobttn1 = Radiobutton(self.frame2_srch_act_frame, text="triangle", variable=self.spattern, value=0)
        self.spattern_radiobttn2 = Radiobutton(self.frame2_srch_act_frame, text="square", variable=self.spattern, value=1)
        self.spattern_radiobttn3 = Radiobutton(self.frame2_srch_act_frame, text="pentagon", variable=self.spattern, value=2)
        self.spattern_radiobttn1.grid(row=2,column=0)
        self.spattern_radiobttn2.grid(row=2,column=1)
        self.spattern_radiobttn3.grid(row=2,column=2)

        self.do_search_bttn = Button(self.frame2_srch_act_frame, text ="Do Search", command=self.do_searchwalk)
        self.cancel_search_bttn = Button(self.frame2_srch_act_frame, text ="Cancel Search", command=self.cancel_searchwalk)
        # adjust elements in grid
        self.do_search_bttn.grid(row=3,column=0)
        self.cancel_search_bttn.grid(row=3,column=1)

        self.input_sw_tlat.set(43.6588224)
        self.input_sw_tlon.set(-79.3792462)
        self.input_srad.set(5.0)
        self.input_srad.set(0)
        #def_coords: (43.6588224, -79.3792462), srad: 5.0, spttrn: 0 

    def do_searchwalk(self):
        """
        get all vals from searchwalk inputfields
        """
        lat = float(self.input_sw_tlat.get())
        lon = float(self.input_sw_tlon.get())
        srad = float(self.input_srad.get())
        spattrn = self.spattern.get()
        e_cv  = self.enable_artag.get()
        e_oa = self.enable_obstacle_avoidance.get()

        msg = (lat, lon, srad, spattrn, e_cv, e_oa)
        #print(lat, lon, srad, spattrn, e_cv, e_oa)
        self.base_node.start_searchwalk(msg)

    def cancel_searchwalk(self):
        self.base_node.cancel_searchwalk()

    def do_teleop_button_4(self):
        #stop/standby everything
        self.teleop.do_teleop_func(True)    #fix message type

    def stop_standby_button_3(self):
        #self.base_node.send_goal(10)
        self.teleop.do_teleop_func(False)    #fix message type
        self.base_node.do_teleop(127,127)
        try:
            self.base_node.cancel_miniwalk_goal()
        except:
            print("no goal set")


    def miniwalk_action_button_1(self):
        self.teleop.do_teleop_func(False)
        self.base_node.send_goal_miniwalk(
            float(self.input_tlat.get()),
            float(self.input_tlon.get()),
            float(self.input_geofence.get()))
    
    def cancel_action_button_2(self):
        self.base_node.cancel_miniwalk_goal()

    def send_pwm_msg(self, lpwm, rpwm):
        self.base_node.do_teleop(lpwm, rpwm)

        
    def show_buttons(self, frame):
        #button pub sub buttons
        
        self.button_label_frame = LabelFrame(frame)

        self.button_label_frame.grid(
                row=BUTTON_FRAME_ROW, 
                column=BUTTON_FRAME_COLUMN,
                rowspan=BUTTON_FRAME_ROWSPAN,
                columnspan=BUTTON_FRAME_COLUMNSPAN,
                padx=ACTION_CONSOLE_FRAME_INNER_PADDING_X,
                pady=ACTION_CONSOLE_FRAME_INNER_PADDING_Y)


        self.action_button_2 = Button(
            self.button_label_frame, 
            text="  Do MiniWalk  ",  
            command=self.miniwalk_action_button_1).grid(
                row=ACTION_CONSOLE_BUTTON_MATRIX[0][0],
                column=ACTION_CONSOLE_BUTTON_MATRIX[0][1],
                padx=BUTTON_FRAME_INNER_PADDING_X,
                pady=BUTTON_FRAME_INNER_PADDING_Y,)

        self.cancel_action_button = Button(
            self.button_label_frame, 
            text="Cancel MiniWalk",  
            command=self.cancel_action_button_2).grid(
                row=ACTION_CONSOLE_BUTTON_MATRIX[1][0],
                column=ACTION_CONSOLE_BUTTON_MATRIX[1][1],
                padx=BUTTON_FRAME_INNER_PADDING_X,
                pady=BUTTON_FRAME_INNER_PADDING_Y,)


        self.pub_button = Button(
            self.button_label_frame, 
            text=" Stop/Standby", 
            command=self.stop_standby_button_3).grid(
                row=ACTION_CONSOLE_BUTTON_MATRIX[2][0],
                column=ACTION_CONSOLE_BUTTON_MATRIX[2][1],
                padx=BUTTON_FRAME_INNER_PADDING_X,
                pady=BUTTON_FRAME_INNER_PADDING_Y,
            )
            
        #action service buttons
        self.action_button = Button(
            self.button_label_frame, 
            text="  Do Teleop  ",  
            command=self.do_teleop_button_4).grid(
                row=ACTION_CONSOLE_BUTTON_MATRIX[3][0],
                column=ACTION_CONSOLE_BUTTON_MATRIX[3][1],
                padx=BUTTON_FRAME_INNER_PADDING_X,
                pady=BUTTON_FRAME_INNER_PADDING_Y,)

    def show_rover_info_labels(self, frame):
        self.rover_info_label_frame = LabelFrame(frame)

        self.rover_info_label_frame.grid(
                row=ROVER_INFO_LABEL_FRAME_ROW, 
                column=ROVER_INFO_LABEL_FRAME_COLUMN,
                rowspan=ROVER_INFO_LABEL_FRAME_ROWSPAN,
                columnspan=ROVER_INFO_LABEL_FRAME_COLUMNSPAN,
                padx=ROVER_INFO_FRAME_INNER_PADDING_X,
                pady=ROVER_INFO_FRAME_INNER_PADDING_Y)

        """ labels """

        self.rover_lat_label = Label(
            self.rover_info_label_frame,
            text="rlat:")
        self.rover_lat_label.grid(
            row=ROVER_LAT_LABEL_ROW,
            column=ROVER_LAT_LABEL_COLUMN,
            padx=ROVER_LAT_LABEL_PADDING_X,
            pady=ROVER_LAT_LABEL_PADDING_Y)

        self.rover_lon_label = Label(
            self.rover_info_label_frame,
            text="rlon:")
        self.rover_lon_label.grid(
            row=ROVER_LON_LABEL_ROW,
            column=ROVER_LON_LABEL_COLUMN,
            padx=ROVER_LON_LABEL_PADDING_X,
            pady=ROVER_LON_LABEL_PADDING_Y)

        self.rover_arb_label = Label(
            self.rover_info_label_frame,
            text="arb:")
        self.rover_arb_label.grid(
            row=ROVER_ARB_LABEL_ROW,
            column=ROVER_ARB_LABEL_COLUMN,
            padx=ROVER_ARB_LABEL_PADDING_X,
            pady=ROVER_ARB_LABEL_PADDING_Y)


        """ data """
        
        self.rover_lat_data = Label(
            self.rover_info_label_frame,
            text="")
        self.rover_lat_data.grid(
            row=ROVER_LAT_DATA_ROW,
            column=ROVER_LAT_DATA_COLUMN,
            padx=ROVER_LAT_DATA_PADDING_X,
            pady=ROVER_LAT_DATA_PADDING_Y)

        self.rover_lon_data = Label(
            self.rover_info_label_frame,
            text="")
        self.rover_lon_data.grid(
            row=ROVER_LON_DATA_ROW,
            column=ROVER_LON_DATA_COLUMN,
            padx=ROVER_LON_DATA_PADDING_X,
            pady=ROVER_LON_DATA_PADDING_Y)

        self.rover_arb_data = Label(
            self.rover_info_label_frame,
            text="")
        self.rover_arb_data.grid(
            row=ROVER_ARB_DATA_ROW,
            column=ROVER_ARB_DATA_COLUMN,
            padx=ROVER_ARB_DATA_PADDING_X,
            pady=ROVER_ARB_DATA_PADDING_Y)


    def update_rover_lla(self, x,y,z):
        self.rover_lat_data.configure(text=f" {x:.5f} ")
        self.rover_lon_data.configure(text=f" {y:.5f} ")
        self.rover_arb_data.configure(text=f" {z:.4f} ")
    
    
    def update_rover_marker(self, x,y):
        self.rover_marker.set_position(x,y)
        
    
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
            if show_type == b'I01\n':
                id = "[miniwalking]"
            
            d2t = str(msg.d2t)[:6]
            he = str(msg.he)[:6]
            
            self.feedback_scroll.insert(
                END,
                f"{id}:    {d2t}     {he}"+'\n')
            self.feedback_scroll.see('end')

    def print_result(self, caller, result):
        print(f"{caller}", result)

    def insert_in_scroll(self, data):
        data = str(data)
        self.event_scroll.insert(END,"rec:   "+data+'\n')
        self.event_scroll.see('end')


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



    def draw_gui(self):
        self.show_map()
        
        self.show_scroll()

        self.show_action_console()

        self.show_status_bar()


    