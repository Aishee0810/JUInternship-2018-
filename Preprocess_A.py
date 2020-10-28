# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:07:10 2018

@author: admin
"""
import os,os.path
import glob
import cv2
#for n in range(97,123)
cpt=231
#images=[]
for p in range(232,267):
    filename1 = chr(70)+'\\'+chr(110)+'\\depth'
    imageDir = 'E:\\3. ASL_O\\Database B\\'+filename1+'_5_'+str('{0:04}'.format(p))+'.png'
#for file in glob.glob(imageDir+"*.png"):
    #images=[file]
    #for imagePath in images:
    im = cv2.imread(imageDir,0)
    print(imageDir)
    row_count, column_count = im.shape
    for x in xrange (row_count):
        for y in range (column_count):
            pixel=im[x,y]
            if pixel in range(1,3):
                im[x,y]=0
            else:
                im[x,y]=255
    opimagePath1='E:\\3. ASL_O\\Database B\\'+chr(70)+'\\'+chr(110)
    #print(opimagePath1)
    cv2.imwrite(os.path.join(opimagePath1, "contour_%04i.png" %cpt), im)
    cpt += 1   
cv2.waitKey(0)
cv2.destroyAllWindows()