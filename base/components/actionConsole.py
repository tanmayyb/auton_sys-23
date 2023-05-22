from cgitb import text
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, scrolledtext


from settings.window import *
from settings.grid import *

class actionConsole():
    def __init__(self, parent, window):
        self.window = window
        self.parent = parent
        
        self.show_drive_switch_frame()
        self.show_rover_info_labels()
        self.show_action_console()
        

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
        self.parent.base_node.send_goal_miniwalk(tlat,tlon, geof)

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
        self.enable_artag.set(1)
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
        e_cv  = True if self.enable_artag.get()==1 else False
        e_oa = self.enable_obstacle_avoidance.get()

        msg = (lat, lon, srad, spattrn, e_cv, e_oa)
        #print(lat, lon, srad, spattrn, e_cv, e_oa)
        self.parent.base_node.start_searchwalk(msg)

    def cancel_searchwalk(self):
        self.parent.base_node.cancel_searchwalk()
        self.parent.base.set_rover_state(0)

    def do_teleop_button_4(self):
        #stop/standby everything
        self.parent.teleop.do_teleop_func(True)
        self.parent.base_node.set_rover_state(int(3))

    def stop_standby_button_3(self):
        self.parent.base_node.set_rover_state(0)
        self.parent.teleop.do_teleop_func(False)
        self.parent.base_node.do_teleop(127,127)
        #add cancel conditions here [important]
        self.parent.base_node.cancel_miniwalk_goal()


    def miniwalk_action_button_1(self):
        self.parent.teleop.do_teleop_func(False)
        self.parent.base_node.send_goal_miniwalk(
            float(self.input_tlat.get()),
            float(self.input_tlon.get()),
            float(self.input_geof.get()))
    
    def cancel_action_button_2(self):
        self.parent.base_node.cancel_miniwalk_goal()

    def send_pwm_msg(self, lpwm, rpwm):
        self.parent.base_node.do_teleop(lpwm, rpwm)

        
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

    def show_rover_info_labels(self):
        self.rover_info_label_frame = LabelFrame(self.window)

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

    def show_drive_switch_frame(self):
        self.drive_switch_frame = LabelFrame(
            self.window, 
            text="drive safety")

        self.drive_switch_frame.grid(
                row=DRIVE_SWITCH_FRAME_ROW, 
                column=DRIVE_SWITCH_FRAME_COLUMN,
                rowspan=DRIVE_SWITCH_FRAME_ROWSPAN,
                columnspan=DRIVE_SWITCH_FRAME_COLUMNSPAN,
                sticky=DRIVE_SWITCH_FRAME_STICKY )

        self.show_drive_switch_buttons()

    
    def show_drive_switch_buttons(self):

        self.e_stop_button = Button(
            self.drive_switch_frame, 
            text="  ENABLE  ",  
            command=self.drive_enable).pack()

        self.e_stop_button = Button(
            self.drive_switch_frame, 
            text="  E-STOP  ",  
            command=self.drive_e_stop).pack()

    def drive_e_stop(self):
        self.parent.base_node.trigger_e_stop()

    def drive_enable(self):
        self.parent.base_node.enable_drive()

    def update_rover_lla(self, x,y,z):
        self.rover_lat_data.configure(text=f" {x:.5f} ")
        self.rover_lon_data.configure(text=f" {y:.5f} ")
        self.rover_arb_data.configure(text=f" {z:.4f} ")
    