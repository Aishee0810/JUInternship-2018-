# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:39:41 2018

@author: admin
"""
import numpy as np
import cv2
import imutils
im = cv2.imread('E:\\3. ASL_O\\Database A\\A\\x\\contour_0000.png',0)
im = cv2.GaussianBlur(im, (5, 5), 0)
# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)
 
# find contours in thresholded image, then grab the largest
# one
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
c = max(cnts, key=cv2.contourArea)
im = cv2.bilateralFilter(im,50,75,75)
ret,thresh = cv2.threshold(im,0,0,cv2.THRESH_BINARY)
im=255-im
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(im, contours, -1, (0,0,255), 10)
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
