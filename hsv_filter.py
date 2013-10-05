# Image Color filter in HSV Space. Use it to find the range of HSV values for hand

import cv2
import numpy as np

def nothing(x):
	pass

# Create a black image, a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('Hmin','image',0,180,nothing)
cv2.createTrackbar('Hmax','image',0,180,nothing)
cv2.createTrackbar('Smin','image',0,255,nothing)
cv2.createTrackbar('Smax','image',0,255,nothing)
cv2.createTrackbar('Vmin','image',0,255,nothing)
cv2.createTrackbar('Vmax','image',0,255,nothing)

vc = cv2.VideoCapture(0)

ret, frame = vc.read()

while ret:
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#reading values
	hmin = cv2.getTrackbarPos('Hmin','image')
	hmax = cv2.getTrackbarPos('Hmax','image')
	smin = cv2.getTrackbarPos('Smin','image')
	smax = cv2.getTrackbarPos('Smax','image')
	vmin = cv2.getTrackbarPos('Vmin','image')
	vmax = cv2.getTrackbarPos('Vmax','image')

	min = np.array([hmin, smin, vmin], np.uint8)
	max = np.array([hmax, smax, vmax], np.uint8)

	filtered = cv2.inRange(hsv, min, max)

	cv2.imshow('image',filtered)
	rval, frame = vc.read()

	key = cv2.waitKey(20)
	if key == 27:
		break

cv2.destroyAllWindows()