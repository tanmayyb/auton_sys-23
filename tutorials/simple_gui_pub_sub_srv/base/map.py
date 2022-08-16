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
map_widget.set_marker(43.65897373429778, -79.37932931217927, text="Ryerson Uni")
map_widget.set_zoom(20)

root_tk.mainloop()

