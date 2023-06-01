import tkintermapview
import os


# This scripts creates a database with offline tiles.

#TMU
# tl_coords = (43.65939, -79.38062)
# br_coords = (43.65823, -79.37881) 
# db_name = "offline_tiles_tmu.db"

#MDRS
tl_coords = (38.40701179562584, -110.79282616484986) 
br_coords = (38.40701179562584, -110.79282616484986) 
db_name = "site_A_off_tiles.db"

top_left_position = (tl_coords[0], tl_coords[1])
bottom_right_position = (br_coords[0], br_coords[1])
zoom_min = 19
zoom_max = 20

# specify path and name of the database
script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, db_name)

# create OfflineLoader instance
loader = tkintermapview.OfflineLoader(path=database_path)

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