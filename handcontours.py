# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:17:01 2018

@author: admin
"""
import glob
import cv2
import numpy
import os, os.path
from matplotlib import pyplot as plt
im=cv2.imread('E:\\3. ASL_O\\Database A\\A\\a\\depth_0_0001.png',0)
plt.hist(im.ravel(),256,[0,5]); plt.show()
row_count, column_count = im.shape
for i in xrange (row_count):
    for j in range (column_count):
        pixel=im[i,j]
        if pixel in range(1,3):
            im[i,j]=0
        else:
            im[i,j]=255
#im = cv2.bilateralFilter(im,20,75,75)
#            im=255-im
#ret,thresh = cv2.threshold(im,-1,0,cv2.THRESH_BINARY)
#im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(im, contours, -1, (0,0,255), 3)
cv2.imshow('image',im)
            #cv2.imwrite('C:\\Users\\Soumi\\Pictures\Screenshots'+filename+'.png',im)
cv2.waitKey(0)
cv2.destroyAllWindows()