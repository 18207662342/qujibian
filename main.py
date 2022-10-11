import numpy as np
import cv2 as cv

K = np.zeros((3, 3))
K[0, 0] = 3685.352203
K[1, 1] = 3685.352203
K[0, 2] = 2725.86
K[1, 2] = 1824.42
K[2, 2] = 1

distCoeffs = np.float32([-0.280892000000, 0.132348000000, 0.000916079000, -0.000695559000, -0.047167700000])

img = cv.imread('1.JPG')
img_undistored = cv.undistort(img, K, distCoeffs)
cv.imwrite('11.JPG', img_undistored)
