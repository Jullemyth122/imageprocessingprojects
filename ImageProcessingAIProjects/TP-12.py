# Histograms Images
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/alb2.jpg')
img = cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)

cv.imshow('Cat',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('gray',gray)

gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)