RESIZE_FACTOR = 2

#IMAGE_NAME = "test.png"
IMAGE_NAME = "multi_aruco_tags.jpg"
IMAGE_NAME = "ME4yS.jpg"
#IMAGE_NAME = "example1.jpeg"
#IMAGE_NAME = "WIN_20221109_13_56_59_Pro.jpg"


IMAGE_NAME_PREFIX = "img/src/"
IMAGE_PATH = IMAGE_NAME_PREFIX+IMAGE_NAME
#IMAGE_ORIGINAL_DIMS = (640, 480)
#IMAGE_ORIGINAL_DIMS = (851, 1134) #for example1
#IMAGE_ORIGINAL_DIMS = (1920, 1080)
IMAGE_ORIGINAL_DIMS = (446, 413) #for ME4yS


IMAGE_RESIZE_DIMS = (RESIZE_FACTOR*IMAGE_ORIGINAL_DIMS[0], RESIZE_FACTOR*IMAGE_ORIGINAL_DIMS[1])