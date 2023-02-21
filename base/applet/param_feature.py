import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import *
import rclpy
from nodes.paramManager import *

import threading

class featureGUI():
    def __init__(self, master, node):  
        self.master = master
        self.node = node

        self.param = self.loadWin()

        #Frame for save button
        frame_save = tk.Frame(
            master = self.master,
            relief = tk.FLAT,
            highlightthickness = 2,
            highlightbackground = "black", 
            highlightcolor = "black"
        )

        #Frame for load button
        frame_load = tk.Frame(
            master = self.master,
            relief = tk.FLAT,
            highlightthickness = 2,
            highlightbackground = "black", 
            highlightcolor = "black"
        )

        #Placing frames into the grid
        frame_save.grid(row = 0, column = 2, padx = 5, pady = 5)
        frame_load.grid(row = 1, column = 2, padx = 5, pady = 5)

        #Setting attributes for Save button
        self.button_save = tk.Button(
            text = "Save",
            master = frame_save,
            font = ('Arial', 25),
            command = lambda: threading.Thread(target=self.save, daemon=True).start()
        )

        #Setting attributes for Load button
        self.button_load = tk.Button(
            text = "Load",
            master = frame_load,
            font = ('Arial', 25),
            command = lambda: threading.Thread(target=self.load, daemon=True).start()
        )

        self.button_save.pack()
        self.button_load.pack()
    
    #Enables all buttons on the GUI
    def btON(self):
        self.button_save.configure(state=tk.NORMAL)
        self.button_load.configure(state=tk.NORMAL)
    
    #Disables all buttons on the GUI
    def btOFF(self):
        self.button_save.configure(state=tk.DISABLED)
        self.button_load.configure(state=tk.DISABLED)

    #Runs when the load button is clicked --> Loads all values from JSON into the GUI
    def load(self):
        self.btOFF()
      
        try:
            self.param = self.node.sendRequest()
        except:
            tk.messagebox.showerror(master = self.master, title = "Error", message = "SERVICE TIMEOUT, could not find service callback")
            self.btON()
            return

        param_names = list(self.param.keys())

        for i in param_names:
            value = self.master.grid_slaves(row = param_names.index(i), column = 1)[0].winfo_children()[0]
            value.delete(0, tk.END)
            value.insert(0, self.param[i])

        self.btON()
        
    #Runs when the save button is clicked (Saves all values in the GUI to JSON)
    def save(self):
        self.btOFF()
            
        param_names = list(self.param.keys())

        for i in param_names:
            #Locates the desired entry widget in the grid and retrieves the value
            #grid_slaves() --> returns the frame that was placed at that grid location in a list, thus why [0] is used at the end
            #winfo_children() --> returns the ordering of widgets inside the frame as a list
            value = self.master.grid_slaves(row = param_names.index(i), column = 1)[0].winfo_children()[0].get()
            
            #Check to see if all inputs are integer values, if not a popup error message will show
            try:
                self.param[i] = float(value)
            except:
                tk.messagebox.showerror(master = self.master, title = "Error", message = "Input Error at " + f"{i}")
        
        self.node.sendParam(self.param)
        self.btON()

    #This functions deals with loading all the information(key and values) from the JSON file into the GUI
    def loadWin(self):

        #Intialize the dictionary from the JSON file
        param = self.node.sendRequest()

        #Gets the name of every key in the dictionary
        param_names = list(param.keys())
       
        #loading parameters into the GUI in a grid form
        for i in range(len(param_names)):
            self.master.columnconfigure(i, weight = 1)
            self.master.rowconfigure(i, weight = 1)
            for x in range(2):
                frame = tk.Frame(
                    master = self.master,
                    relief = tk.FLAT,
                    borderwidth = 5
                )
                frame.grid(row = i, column = x, padx = 5, pady = 5)

                if x == 0:
                    label = tk.Label(master = frame, text = param_names[i], highlightthickness = 2)
                    label.config(highlightbackground = "grey", highlightcolor = "grey", font = ('Arial', 25))
                    label.pack()
                elif x == 1:
                    entry = tk.Entry(master = frame, highlightthickness = 2, justify = "center")
                    entry.config(highlightbackground = "black", highlightcolor = "black", font = ('Arial', 25) )
                    entry.pack()
                    entry.insert(0, param[param_names[i]])
        
        return param
        
def launchFWindow(master): #Main function that launches the feature window
    try:
        newWindow = tk.Toplevel(master) #Links the new window with the original window
        newWindow.title("Parameter Controls")
        newWindow.minsize(800,500)    
        node = PublisherClient() #Init the publisher_client node
        app = featureGUI(newWindow, node) #launches the window
    except:
        tk.messagebox.showerror(title = "Error", message = "SERVICE TIMEOUT, could not find service callback")
    
    newWindow.wait_window() #this function is used to wait for the feature window to close (it halts the code from executing the rest of the code)
    node.destroy_node() #destroys all node used in the feature window
    
