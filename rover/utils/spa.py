"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Main Auth:  Niko Trivanovic
Created:    15 January, 2023
Search Pattern Algorithm (S.P.A) for SearchWalk
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

import math

def generateSearchPattern(searchwalk_goal, verbose=False):

    """
    algorithm default constants, determined by experimentation
    """
    center_coord, radius, pattern = searchwalk_goal
    #print("spa: ", center_coord, radius, pattern)
    #SearchWalk pattern constants
    slope = 0.2
    scale = 0.00001
    theta = 0
    step_jump = slope*radius + 1.0 #step jump scaling equation
    step = 1
    step_angle = 120.0 #default
    #find step angle
    if(pattern==0): step_angle = 120.0
    elif(pattern==1): step_angle = 90.0
    elif(pattern==2): step_angle = 72.0
    searchwalk_points = [center_coord]
    num_search_points = int((radius//step_jump) * (360.0//step_angle))
    
    if(verbose): print("spa: \tnum_search_points: ", num_search_points)
    try:
        for n in range(num_search_points):
            if theta >= 360.0:
                theta = 0
                step += 1
            lat = center_coord[0] + (((step * step_jump) * math.cos(math.radians(theta)))*scale) 
            lon = center_coord[1] + (((step * step_jump) * math.sin(math.radians(theta)))*scale)
            searchwalk_points.append((lat,lon))
            theta += step_angle
            """
            Tool to plot SEARCHPOINTS: 
            https://maps.co/gis/
            """
            #print(lat,",",lon)
    except:
        print('generateSearchPattern: error creating searchwalk_points')
    return searchwalk_points