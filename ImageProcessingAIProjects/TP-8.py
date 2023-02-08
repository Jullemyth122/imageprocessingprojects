# Split Mergy images
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
resized = cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)
cv.imshow('Image',resized)

blank = np.zeros(resized.shape[:2],dtype='uint8')

b,g,r = cv.split(resized)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([r,r,r])

cv.imshow('Blue Cast',blue)
cv.imshow('Green Cast',green)
cv.imshow('red cast',red)

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merged = cv.merge([b,b,g])
merged = cv.merge([b,g,r])
# merged = cv.merge([b,r,b])
# merged = cv.merge([r,b,b])
# merged = cv.merge([g,g,r])
# merged = cv.merge([b,g,g])
# merged = cv.merge([b,r,r])
# merged = cv.merge([r,g,r])
# merged = cv.merge([r,r,b])
cv.imshow("Merge Image",merged)

cv.waitKey(0)