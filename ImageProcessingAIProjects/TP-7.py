# Spaces colors
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
resized = cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)
cv.imshow('Image',resized)


# grayscale
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow("Rock Band Gray",gray)

# BGR to HSV
hsv = cv.cvtColor(resized,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to L*a*b
lab = cv.cvtColor(resized,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# BGR to RGB
rgb = cv.cvtColor(resized,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSVtoBGR',hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LABtoBGR',lab_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)