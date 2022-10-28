# python program for prewitt edge detection using opencv and numpy
import cv2
import numpy as np

# Read the original image
img = cv2.imread('P01.jpg') 
# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

# prewitt edge detection
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_blur, -1, kernelx) # edge detection on x axis
img_prewitty = cv2.filter2D(img_blur, -1, kernely) # edge detection on y axis
img_prewittxy = img_prewittx + img_prewitty #e dge detection on both axis

# Display prewitt edge detection images
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt XY", img_prewittxy)

cv2.waitKey(0)
cv2.destroyAllWindows()