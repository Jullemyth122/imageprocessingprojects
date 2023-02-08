# Contour Detection
import cv2 as cv
import numpy as np

img = cv.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
resized = cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)

blank = np.zeros(resized.shape,dtype='uint8')

# grayscale
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow("Rock Band Gray",gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

ret,thresh = cv.threshold(gray, 125, 255,cv.THRESH_BINARY)
cv.imshow('threshold',thresh)

# contours, hierarchies = cv.findContours(canny,cv.RETR_CCOMP)
# contours, hierarchies = cv.findContours(canny,cv.RETR_EXTERNAL)
# contours, hierarchies = cv.findContours(canny,cv.RETR_FLOODFILL)
# contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# contours, hierarchies = cv.findContours(canny,cv.RETR_TREE)


# contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)