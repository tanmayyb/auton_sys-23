import tkinter, tkintermapview
import os


# This scripts creates a database with offline tiles.

#TMU
# tl_coords = (43.65939, -79.38062)
# br_coords = (43.65823, -79.37881) 
# coords = (43.65897373429778, -79.37932931217927) 
# db_name = "offline_tiles_tmu.db"

#MDRS
tl_coords = (38.40701179562584, -110.79282616484986) 
br_coords = (38.40701179562584, -110.79282616484986) 
coords = (38.40701179562584, -110.79282616484986) 
db_name = "site_A_off_tiles.db"

# tile_server = None

#tile_server = "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png" #osm 
#tile_server = "https://api.maptiler.com/tiles/satellite-v2/?key=rVXTQlO038F9qqhaVy8V#0.8/-0.20297/-5.88618"
tile_server = "https://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}&s=Ga"
#tile_server = ""


top_left_position = (tl_coords[0], tl_coords[1])
bottom_right_position = (br_coords[0], br_coords[1])
zoom_min = 19
zoom_max = 22

# specify path and name of the database
script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, db_name)

# create OfflineLoader instance
loader = tkintermapview.OfflineLoader(tile_server=tile_server, path=database_path)

# save the tiles to the database, an existing database will extended
loader.save_offline_tiles(
    top_left_position, 
    bottom_right_position, 
    zoom_min, 
    zoom_max)

# You can call save_offline_tiles() multiple times and load multiple regions into the database.
# You can also pass a tile_server argument to the OfflineLoader and specify the server to use.
# This server needs to be then also set for the TkinterMapView when the database is used.
# You can load tiles of multiple servers in the database. Which one then will be used depends on
# which server is specified for the TkinterMapView.

# print all regions that were loaded in the database
loader.print_loaded_sections()







# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("map_view_simple_example.py")

# path for the database to use
script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, db_name)

# create map widget and only use the tiles from the database, not the online server (use_database_only=True)
map_widget = tkintermapview.TkinterMapView(root_tk, 
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