#THRESHOLDING + FILTERING ( DENOISE )

import cv2
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'TkAgg' 


import matplotlib.pyplot as plt


#img = cv2.imread('/home/pi/Desktop/images/noise1.jpg',0)

def denoise(img):
# global thresholding
 ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
 ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
 blur = cv2.GaussianBlur(img,(5,5),0)
 ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
 cv2.imshow("global", th1)
 cv2.imshow("otsu thresholding", th2)
 cv2.imshow("after filtering",th3)
 cv2.imshow("orignal", img)
 cv2.waitKey(0)

# plot all the images and their histograms
 images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
 titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

 for i in xrange(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
 plt.show()
 
 cv2.imwrite("/home/pi/Desktop/denoised.jpg", th3)
 
 return th3
 





