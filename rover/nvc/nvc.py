"""
Main Auth: Tanmay B.

"""

from math import sin, cos, atan2, radians, degrees, sqrt


def nv_calc(current_coords, target_coords):


    R = 6371000.0  # radius of Earth in meters

    """
    Find bearing:
    code for angle calc starts here 
    """
    x1 = current_coords[0]     #:lat
    y1 = current_coords[1]     #:lon

    x2 = target_coords[0]      #:lat
    y2 = target_coords[1]      #:lon
    
    theta_x1 = radians(x1)     #:lat_x1
    theta_x2 = radians(x2)     #:lat_x2
    
    dX = radians(x2-x1)
    dL = radians(y2-y1)
    
    #print(x1,x2,y1,y2)

    X = cos(theta_x2)*sin(dL)
    Y = cos(theta_x1)*sin(theta_x2) - sin(theta_x1)*cos(theta_x2)*cos(dL)

    heading = atan2(X,Y)

    """
    Find distance to target:
    use havesine to find distance between coords
    """

    a = sin(dX / 2.0) ** 2 + cos(theta_x1) * cos(theta_x2) * sin(dL / 2.0) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c  # output distance in meters
    
    return degrees(heading), distance

"""
Resources used:
Bearing calculation:
https://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/
https://www.igismap.com/map-tool/bearing-angle

Haversine Distance formula:
https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128
https://www.movable-type.co.uk/scripts/latlong.html
"""

