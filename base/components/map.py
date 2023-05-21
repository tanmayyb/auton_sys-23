from cgitb import text
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, scrolledtext

import tkintermapview
import time


from settings.window import *
from settings.grid import *

import os


class map():
    def __init__(self, parent, window):
        self.window = window
        self.parent = parent

        self.home = (TMU_LAT, TMU_LON)

        self.waypoints = 0
        self.markers = []
        self.path = None

        self.show_map()
    
    def show_map(self):
        script_directory = os.path.dirname(os.path.abspath("base/components"))
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
                columnspan=MAP_FRAME_COLUMNSPAN,
                sticky=MAP_STICKY)

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
        self.parent.actionConsole.input_tlat.set(str(coords[0]))
        self.parent.actionConsole.input_tlon.set(str(coords[1]))

        self.parent.actionConsole.input_sw_tlat.set(str(coords[0]))
        self.parent.actionConsole.input_sw_tlon.set(str(coords[1]))

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

        self.parent.base_node.send_goal_miniwalk(
            float(coords[0]),
            float(coords[1]),
            float(self.parent.actionConsole.input_geof.get()))

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


    def update_rover_marker(self, x,y):
        #called by nodes/base.py/gui_update_rover_lla()
        self.rover_marker.set_position(x,y)