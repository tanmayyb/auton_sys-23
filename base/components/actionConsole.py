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

        self.show_action_console()
    
    def show_action_console(self):
        self.action_console_frame = LabelFrame(
            self.window,
            text="action console")
        self.action_console_frame.grid(
                row=ACTION_CONSOLE_FRAME_ROW, 
                column=ACTION_CONSOLE_FRAME_COLUMN,
                rowspan=ACTION_CONSOLE_FRAME_ROWSPAN,
                columnspan=ACTION_CONSOLE_FRAME_COLUMNSPAN,
                sticky=ACTION_CONSOLE_FRAME_STICKY)

        self.show_text_fields(self.action_console_frame)
        self.show_buttons(self.action_console_frame)
        self.show_rover_info_labels(self.action_console_frame)

    
    def show_text_fields(self, frame):
        
        self.text_field_labels = LabelFrame(frame)
        self.text_fields = LabelFrame(frame)


        """TEXT FIELD LABELS"""
        self.text_field_labels.grid(
                row=TEXT_FIELD_LABEL_FRAME_ROW, 
                column=TEXT_FIELD_LABEL_FRAME_ROW, 
                padx=ACTION_CONSOLE_FRAME_INNER_PADDING_X,
                pady=ACTION_CONSOLE_FRAME_INNER_PADDING_Y)

        self.input_geofence_label = Label(
            self.text_field_labels, 
            text="Input Geofence")
        self.input_geofence_label.pack(
            padx=TEXT_FIELD_LABEL_FRAME_INNER_PADDING_X,
            pady=TEXT_FIELD_LABEL_FRAME_INNER_PADDING_Y)

        self.input_tlat_label = Label(
            self.text_field_labels, 
            text="Input Target Lat")
        self.input_tlat_label.pack(
            padx=TEXT_FIELD_LABEL_FRAME_INNER_PADDING_X,
            pady=TEXT_FIELD_LABEL_FRAME_INNER_PADDING_Y)


        self.input_tlat_label = Label(
            self.text_field_labels, 
            text="Input Target Lon")
        self.input_tlat_label.pack(
            padx=TEXT_FIELD_LABEL_FRAME_INNER_PADDING_X,
            pady=TEXT_FIELD_LABEL_FRAME_INNER_PADDING_Y)


        """TEXT FIELDS"""
        self.text_fields.grid(
                row=TEXT_FIELDS_FRAME_ROW, 
                column=TEXT_FIELDS_FRAME_COLUMN, 
                padx=ACTION_CONSOLE_FRAME_INNER_PADDING_X,
                pady=ACTION_CONSOLE_FRAME_INNER_PADDING_Y)

        self.input_geofence = StringVar()
        self.input_geofence_textbox = Entry(
            self.text_fields, 
            textvariable=self.input_geofence)
        self.input_geofence_textbox.pack(
            padx=TEXT_FIELDS_FRAME_INNER_PADDING_X,
            pady=TEXT_FIELDS_FRAME_INNER_PADDING_Y)

        self.input_tlat = StringVar()
        self.input_tlat_textbox = Entry(
            self.text_fields, 
            textvariable=self.input_tlat)
        self.input_tlat_textbox.pack(
            padx=TEXT_FIELDS_FRAME_INNER_PADDING_X,
            pady=TEXT_FIELDS_FRAME_INNER_PADDING_Y)

        self.input_tlon = StringVar()
        self.input_tlon_textbox = Entry(
            self.text_fields, 
            textvariable=self.input_tlon)
        self.input_tlon_textbox.pack(
            padx=TEXT_FIELDS_FRAME_INNER_PADDING_X,
            pady=TEXT_FIELDS_FRAME_INNER_PADDING_Y)

        self.input_geofence.set("2.0")
        self.input_tlat.set("43.6587021")
        self.input_tlon.set("-79.3792810")

        #KWAD CENTER
        #43.6587021
        #-79.3792810
        
    def do_teleop_button_4(self):
        #stop/standby everything
        self.parent.teleop.do_teleop_func(True)    #fix message type

    def stop_standby_button_3(self):
        #self.base_node.send_goal(10)
        self.parent.teleop.do_teleop_func(False)    #fix message type
        self.parent.base_node.do_teleop(127,127)
        try:
            self.parent.base_node.cancel_miniwalk_goal()
        except:
            print("no goal set")


    def miniwalk_action_button_1(self):
        self.parent.teleop.do_teleop_func(False)
        self.parent.base_node.send_goal_miniwalk(
            float(self.input_tlat.get()),
            float(self.input_tlon.get()),
            float(self.input_geofence.get()))
    
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