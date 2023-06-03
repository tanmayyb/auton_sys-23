import tkinter
import os
from tkintermapview import TkinterMapView


#TMU
#coords = (43.65897373429778, -79.37932931217927) 
#db_name = "offline_tiles_tmu.db"

#MDRS
coords = (38.40714534649276, -110.79057649597202) 
db_name = "offline_mdrs.db"

#GREEN RIVER
#coords = (38.99347971713025, -110.13929946458637) 
#db_name = "offline_green_river.db"

#SITE A
#coords = (38.420255, -110.784279)

#SITE B
#coords = (38.421601, -110.784859)

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
#map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=19)  # google satellite
map_widget.pack(fill="both", expand=True)


#map_widget.set_address("nyc")

map_widget.set_position(coords[0], coords[1])  
map_widget.set_marker(
    coords[0],
    coords[1], 
    text="Location")
map_widget.set_zoom(19)

root_tk.mainloop()