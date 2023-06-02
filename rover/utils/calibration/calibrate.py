from charuco import calibrate_charuco
from utils.utils import load_coefficients, save_coefficients
import cv2, os


CamName = 'gucc'
# Parameters
IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'imgs', CamName)
IMAGES_FORMAT = '.jpg'
# Dimensions in cm
MARKER_LENGTH = 0.8
SQUARE_LENGTH = 1


# Calibrate 
ret, mtx, dist, rvecs, tvecs = calibrate_charuco(
    IMAGES_DIR, 
    IMAGES_FORMAT,
    MARKER_LENGTH,
    SQUARE_LENGTH
)


CALIB_DIR = 'rover/utils/calibration'
YML_DIR = os.path.join(CALIB_DIR, 'calibration_charuco.yml')
# Save coefficients into a file
save_coefficients(mtx, dist, YML_DIR)

# Load coefficients
mtx, dist = load_coefficients(YML_DIR)

DIST_IMG_DIR = os.path.join(CALIB_DIR, 'dist.jpg')
original = cv2.imread(DIST_IMG_DIR)
dst = cv2.undistort(original, mtx, dist, None, mtx)
UNDIST_IMG_DIR = os.path.join(CALIB_DIR, 'undist.jpg')
cv2.imwrite(UNDIST_IMG_DIR, dst)