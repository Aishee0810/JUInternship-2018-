# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import glob
import cv2
import numpy
import os, os.path
for p in range(65,70):
    for q in range(97,122):
        cpt=0
        images=[]
        filename1 = chr(p)+'\\'+chr(q)+'\\depth'
        imageDir = 'E:\\3. ASL_O\\Database A\\'+filename1
        for file in glob.glob(imageDir+"*.png"):
            images=[file]
            for imagePath in images:
                im = cv2.imread(imagePath,0)
                print(imagePath)
                row_count, column_count = im.shape
                for i in xrange (row_count):
                    for j in range (column_count):
                        pixel=im[i,j]
                        if pixel in range(1,4):
                            im[i,j]=0
                        else:
                            im[i,j]=255
                opimagePath='E:\\3. ASL_O\\Database A\\'+chr(p)+'\\'+chr(q)
                cv2.imwrite(os.path.join(opimagePath, "contour_%04i.png" %cpt), im)
                cpt += 1      
for m in range(65,74):
    for n in range(97,123):
        cpt1=0
        images1=[]
        filename2 = chr(p)+'\\'+chr(q)+'\\depth'
        imageDir1 = 'E:\\3. ASL_O\\Database B\\'+filename2
        for file in glob.glob(imageDir1+"*.png"):
            images1=[file]
            for imagePath1 in images1:
                im1 = cv2.imread(imagePath1,0)
                print(imagePath1)
                row_count1, column_count1 = im1.shape
                for x in xrange (row_count1):
                    for y in range (column_count1):
                        pixel1=im1[x,y]
                        if pixel1 in range(1,4):
                            im1[x,y]=0
                        else:
                            im1[x,y]=255
                opimagePath1='E:\\3. ASL_O\\Database B\\'+chr(p)+'\\'+chr(q)
                cv2.imwrite(os.path.join(opimagePath1, "contour_%04i.png" %cpt1), im)
                cpt1 += 1      
cv2.waitKey(0)
cv2.destroyAllWindows()
