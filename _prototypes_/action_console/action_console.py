from tkinter import *
from tkinter.ttk import *

# root window
root = Tk()
root.geometry('800x400')

# create a notebook
actions_notebook = Notebook(root)
actions_notebook.pack(pady=10, expand=True)

# create frames for action consoles
miniwalk_frame = Frame(actions_notebook, width=600, height=280)
srch_act_frame = Frame(actions_notebook, width=600, height=280)

"""
frames of miniwalk tab
"""
frame1_miniwalk_frame = LabelFrame(miniwalk_frame)
frame2_miniwalk_frame = LabelFrame(miniwalk_frame)
frame1_miniwalk_frame.grid(row=0,column=0)
frame2_miniwalk_frame.grid(row=0,column=1)

"""
elements of frame 1 of miniwalk
"""
# labels 
input_srad_label1 = Label(frame1_miniwalk_frame, text = "Input GeoF")
input_tlat_label1 = Label(frame1_miniwalk_frame, text = "Input TLat")
input_tlon_label1 = Label(frame1_miniwalk_frame, text = "Input TLon")
input_srad_label1.grid(row=0,column=0)
input_tlat_label1.grid(row=1,column=0)
input_tlon_label1.grid(row=2,column=0)

#text fields
input_geof1 = Entry(frame1_miniwalk_frame)
input_tlat1 = Entry(frame1_miniwalk_frame)
input_tlon1 = Entry(frame1_miniwalk_frame)
# adjust elements in grid
input_geof1.grid(row=0,column=1,columnspan=4)
input_tlat1.grid(row=1,column=1,columnspan=4)
input_tlon1.grid(row=2,column=1,columnspan=4)

"""
elements of frame 2 of miniwalk
"""
do_miniwalk_bttn = Button(frame2_miniwalk_frame, text ="Do Miniwalk")
cancel_miniwalk_bttn = Button(frame2_miniwalk_frame, text ="Cancel Miniwalk")
# adjust elements in grid
do_miniwalk_bttn.grid(row=0,column=0)
cancel_miniwalk_bttn.grid(row=1,column=0)


"""
frames of search tab
"""
# add elements in the search action frame
frame1_srch_act_frame = LabelFrame(srch_act_frame) #left frame
frame2_srch_act_frame = LabelFrame(srch_act_frame) #right frame
# adjust frames in search action frame grid
frame1_srch_act_frame.grid(row=0, column=0)
frame2_srch_act_frame.grid(row=0, column=1)

"""
elements of frame 1 of searchwalk
"""
# labels 
input_tlat_label2 = Label(frame1_srch_act_frame, text = "Input TLat")
input_tlon_label2 = Label(frame1_srch_act_frame, text = "Input TLon")
input_srad_label2 = Label(frame1_srch_act_frame, text = "Input SRad")
input_tlat_label2.grid(row=0,column=0)
input_tlon_label2.grid(row=1,column=0)
input_srad_label2.grid(row=2,column=0)

#text fields
input_tlat2 = Entry(frame1_srch_act_frame)
input_tlon2 = Entry(frame1_srch_act_frame)
input_tlat2.grid(row=0,column=1,columnspan=4)
input_tlon2.grid(row=1,column=1,columnspan=4)

#radio buttons
srad = IntVar()
srad_radiobttn1 = Radiobutton(frame1_srch_act_frame, text="5m", variable=srad, value=5)
srad_radiobttn2 = Radiobutton(frame1_srch_act_frame, text="10m", variable=srad, value=10)
srad_radiobttn3 = Radiobutton(frame1_srch_act_frame, text="20m", variable=srad, value=20)
srad_radiobttn1.grid(row=2,column=1)
srad_radiobttn2.grid(row=2,column=2)
srad_radiobttn3.grid(row=2,column=3)

"""
elements of frame2 of searchwalk
"""
enable_artag = IntVar()
enable_obstacle_avoidance = IntVar()
spattern = IntVar()

artag_chkbttn = Checkbutton(frame2_srch_act_frame, text='enable_cv',variable=enable_artag, onvalue=1, offvalue=0)
obstacle_avoidance_chkbttn = Checkbutton(frame2_srch_act_frame, text='enable_oa',variable=enable_obstacle_avoidance, onvalue=1, offvalue=0)
# adjust elements in grid
artag_chkbttn.grid(row=0,column=0)
obstacle_avoidance_chkbttn.grid(row=0,column=1)

spattern_radiobttn1 = Radiobutton(frame2_srch_act_frame, text="triangle", variable=spattern, value=0)
spattern_radiobttn2 = Radiobutton(frame2_srch_act_frame, text="square", variable=spattern, value=1)
spattern_radiobttn3 = Radiobutton(frame2_srch_act_frame, text="pentagon", variable=spattern, value=2)
spattern_radiobttn1.grid(row=2,column=0)
spattern_radiobttn2.grid(row=2,column=1)
spattern_radiobttn3.grid(row=2,column=2)

do_search_bttn = Button(frame2_srch_act_frame, text ="Do Search")
cancel_search_bttn = Button(frame2_srch_act_frame, text ="Cancel Search")
# adjust elements in grid
do_search_bttn.grid(row=3,column=0)
cancel_search_bttn.grid(row=3,column=1)


#set frame placement
miniwalk_frame.pack(fill='both', expand=True)
srch_act_frame.pack(fill='both', expand=True)

# add frames to notebook
actions_notebook.add(miniwalk_frame, text='Miniwalk')
actions_notebook.add(srch_act_frame, text='Searchwalk')


root.mainloop()