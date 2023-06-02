import numpy as np
import cv2
import cv2.aruco as aruco
import pathlib
import sys, os


def calibrate_charuco(dirpath, image_format, marker_length, square_length):
    '''Apply camera calibration using aruco.
    The dimensions are in cm.
    '''
    
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    board = aruco.CharucoBoard((7, 5), square_length, marker_length, aruco_dict)
    arucoParams = aruco.DetectorParameters()

    corners_list = []  
    id_list = []

    charuco_corners_list = []  
    charuco_id_list = []


    print("\ncurrent_dir: \n", os.path.dirname(os.path.realpath(__file__)))
    print("\nimg_dir:\n", dirpath)
    img_dir = dirpath
    #print('\nlist files:\n', os.listdir(img_dir), "\n")
    
    # Find the ArUco markers inside each image
    img_gray = None
    
    imgs = os.listdir(img_dir)

    for img in imgs:
        #print(f'using image {img}')
        image = cv2.imread(os.path.join(img_dir, str(img)))
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = aruco.detectMarkers(
            img_gray, 
            aruco_dict, 
            parameters=arucoParams
        )

        corners_list.append(corners)
        id_list.append(ids)
        resp, charuco_corners, charuco_ids = aruco.interpolateCornersCharuco(
            markerCorners=corners,
            markerIds=ids,
            image=img_gray,
            board=board
        )
        # Add these corners and ids to our calibration arrays
        charuco_corners_list.append(charuco_corners)
        charuco_id_list.append(charuco_ids)

    #print("\ncorners list:\n",corners_list,"\nid list:\n ", id_list)
    #print("\ncharuco corners list:\n",corners_list,"\ncharuco id list:\n ", id_list)


    ret, mtx, dist, rvecs, tvecs = aruco.calibrateCameraCharuco(
        charucoCorners=charuco_corners_list, 
        charucoIds=charuco_id_list, 
        board=board, 
        imageSize=img_gray.shape, 
        cameraMatrix=None, 
        distCoeffs=None)
    

    return [ret, mtx, dist, rvecs, tvecs]
