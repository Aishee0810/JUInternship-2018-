# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 13:08:02 2018

@author: admin
"""
import cv2
import glob
import numpy
import os, os.path
for m in range(65,74):
    for n in range(97,123):
        cpt=0
        images=[]
        filename1 = chr(m)+'\\'+chr(n)+'\\depth'
        imageDir = 'E:\\3. ASL_O\\Database B\\'+filename1
        for file in glob.glob(imageDir+"*.png"):
            images=[file]
            for imagePath in images:
                im = cv2.imread(imagePath,0)
            print(imagePath)
            row_count, column_count = im.shape
            for x in xrange (row_count):
                for y in range (column_count):
                    pixel=im[x,y]
                    if m==65 or 69 or 72 :
                        if pixel in range(1,5):
                            im[x,y]=0
                        else:
                            im[x,y]=255
                    elif m==68 or 73:
                        if pixel in range(1,4):
                            im[x,y]=0
                        else:
                            im[x,y]=255
                    else:
                        if pixel in range(1,3):
                            im[x,y]=0
                        else:
                            im[x,y]=255
            opimagePath1='E:\\3. ASL_O\\Database B\\'+chr(m)+'\\'+chr(n)
            cv2.imwrite(os.path.join(opimagePath1, "contour_%04i.png" %cpt), im)
            cpt += 1      
cv2.waitKey(0)
cv2.destroyAllWindows()