from email.mime import image
import tkinter
import tkintermapview

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map_view_example.py")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# set current widget position and zoom
map_widget.set_position(43.65897373429778, -79.37932931217927)  # Ryerson
import tkinter as tk
from tkinter import ANCHOR, ttk


#python_image = tk.PhotoImage(file='dot.png')

#home = map_widget.set_marker(43.65897373429778, -79.37932931217927, text="Ryerson Uni", image=python_image)

home = map_widget.set_marker(43.65897373429778, -79.37932931217927, text="Ryerson Uni")


map_widget.set_zoom(20)

global markers, waypoint, path
markers = []

waypoint = 0
path = None


def add_marker_event(coords):
    print("Add marker:", coords)
    global waypoint, path, markers
    
    waypoint = waypoint+1
    
    new_marker = map_widget.set_marker(coords[0], coords[1], text="wp: "+str(waypoint))
    markers.append(new_marker)

    if waypoint==1:
        path = map_widget.set_path([home.position,markers[0].position])
    if waypoint>1:
        x = markers[waypoint-1].position[0]
        y = markers[waypoint-1].position[1]
        print(x,y)
        path.add_position(x,y)

        
        path.add_position(x,y)
        path.remove_position(x,y)



        

def del_marker_event():
    global waypoint, path, markers
    x = markers[-1].position[0]
    y = markers[-1].position[1]
    path.remove_position(x,y)
    markers[-1].delete()
    markers.pop()
    waypoint= waypoint-1

    

map_widget.add_right_click_menu_command(label="Add Marker",
                                        command=add_marker_event,
                                        pass_coords=True)

                                        
map_widget.add_right_click_menu_command(label="Pop Last Marker",
                                        command=del_marker_event,
                                        pass_coords=False)

root_tk.mainloop()

