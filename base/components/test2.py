import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import *

class featureGUI():
    def __init__(self, master):  
        self.master = master

def launchFWindow(master):
    newWindow = tk.Toplevel(master) #Links the new window with the original window
    newWindow.title("Parameter Controls") 
    newWindow.minsize(800,500)
    app = featureGUI(newWindow)