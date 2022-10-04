import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

#prepare object points
nx = 8 #number of inside corners in x
ny = 6 #number of inside corners in y

# List of calliberatopn images
images = glob.glob('/home/leon/Downloads/RoboND-Perception-Intro-master/Camera_Calibration/cali_small/Cal*.jpg')

# Select an index
idx = 5

# Read in the image
img = mpimg.imread(images[idx])

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Find chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
# If found, draw corners
if ret == True:
    # Draw and display the corners
    cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
    #plt.imshow(img)
    #plt.show()
    cv2.imshow('Image',img)
    k = cv2.waitKey(0)