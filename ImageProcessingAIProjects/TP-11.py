# Masking Images
import cv2 as cv
import numpy as np

img = cv.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
img = cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)

blank = np.zeros(img.shape[:2] ,dtype='uint8')
cv.imshow('Blank Image',blank)

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),250,255,-1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Mask',masked)

cv.waitKey(0)