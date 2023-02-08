# Image transformation
import cv2 as cv
import numpy as np

img = cv.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
resized = cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)

cv.imshow("Rock Band",resized)

# Translation

def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)


# -x --> left
# x --> right
# -y --> up
# y --> down


# translated = translate(resized,x,y)
# translated = translate(resized,-x,-y)
translated = translate(resized,100,100)
cv.imshow('Translated',translated)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotmat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = width,height
    return cv.warpAffine(img,rotmat,dimensions)

rotated_point = rotate(resized,45,(10,10))
cv.imshow('Rotated_Point',rotated_point)

rotated = rotate(resized,45)
cv.imshow('Rotated',rotated)

rotated_rotated = rotate(rotated,-45)
cv.imshow('Rotated Rotated',rotated_rotated)

rotated_rotated_point = rotate(rotated_point,-45,(100,100))
cv.imshow('Rotated Rotated Point',rotated_rotated_point)


cv.waitKey(0)