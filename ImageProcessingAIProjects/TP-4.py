# Functionality 
import cv2 as cv

img = cv.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
cv.imshow("Rock Band",img)

# grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Rock Band Gray",gray)

# blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Rock Band Blue",blur)

# Edge Cascade
canny = cv.Canny(img,125,175)
cannyblur = cv.Canny(blur,125,175)
cv.imshow("Canny Edges",canny)
cv.imshow("Canny Edges Blur",cannyblur)

# Dilating the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilating",dilated)

# Eroding
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroding",eroded)

# Resize(By more clear images)
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)

# Cropped
cropped = resized[50:200,200:400]
cv.imshow('Cropepd',cropped)

cv.waitKey(0)