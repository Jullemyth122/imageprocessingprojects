# For Draw Text.py
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
cv.imshow('Blank',blank)

# All Black the matrices [0,0,0]
# print(blank)
# 1. Point the image a certain colour
# the arrays colors will based on your 2D-3D matrices
# print(blank[:])
# blank[200:350] = 0,0,255

print(blank[:])
# cv.imshow('Green',blank)
# blank[400:500] = 0,255,255
# cv.imshow('Ewan',blank)

# 2. Draw a rectangle
# Borders Only
cv.rectangle(blank,(0,0),(100,100),(0,255,0),thickness=1)
cv.imshow('Rectangle1',blank)

# Filled
cv.rectangle(blank,(0,0),(100,100),(0,255,0),thickness=cv.FILLED)
cv.imshow('Rectangle2',blank)

# 1 / 4 of the blank shape
x,y = blank.shape[0]//2, blank.shape[1]//2
cv.rectangle(
        blank,
        (0,0),
        (x,y),
        (0,255,0),
        thickness=cv.FILLED
)
cv.imshow('Rectangle2',blank)

# 3. Draw A Circle
cv.circle(blank,(x,y),100,(0,0,255),thickness=1)
cv.imshow('Circle',blank)

# 4. Draw A line
cv.line(blank,(0,0),(x,y),(0,0,255),thickness=1)
cv.imshow('Line',blank)
# 5. Write Text
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_COMPLEX,2,(155,155,25),1)
cv.imshow('Text',blank)

cv.waitKey(0)