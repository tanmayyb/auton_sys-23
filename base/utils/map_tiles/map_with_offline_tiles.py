import tkinter
import os
from tkintermapview import TkinterMapView


#TMU
#coords = (43.65897373429778, -79.37932931217927) 
#db_name = "offline_tiles_tmu.db"

#MDRS
coords = (38.40701179562584, -110.79282616484986) 
db_name = "site_A_off_tiles.db"


# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("map_view_simple_example.py")

# path for the database to use
script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, db_name)

# create map widget and only use the tiles from the database, not the online server (use_database_only=True)
map_widget = TkinterMapView(root_tk, 
                            width=1000, 
                            height=700, 
                            corner_radius=0, 
                            use_database_only=True,
                            max_zoom=19, 
                            database_path=database_path)
map_widget.pack(fill="both", expand=True)

#map_widget.set_address("nyc")

map_widget.set_position(coords[0], coords[1])  
map_widget.set_marker(
    coords[0],
    coords[1], 
    text="Location")
map_widget.set_zoom(20)

root_tk.mainloop()