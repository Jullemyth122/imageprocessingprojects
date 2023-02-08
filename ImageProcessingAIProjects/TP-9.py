# Smoothing images
import cv2

img = cv2.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
img = cv2.resize(img,(700,700),interpolation=cv2.INTER_CUBIC)

cv2.imshow('Cats',img)
# cv2.imshow('Cats',img)

# # Average
# average1 = cv2.blur(img,(1,10))
# average2 = cv2.blur(img,(7,7))
average3 = cv2.blur(img,(25,5))
average4 = cv2.blur(img,(25,5),(100,100))
# cv2.imshow('Average Blur1',average1)
# cv2.imshow('Average Blur2',average2)
cv2.imshow('Average Blur3',average3)
cv2.imshow('Average Blur4',average4)

# # Gaussian Blur
# gauss = cv2.GaussianBlur(img,(7,7),0)
# cv2.imshow('Gaussian Blur',gauss)

# # Median Blur
# median = cv2.medianBlur(img,7,0)
# cv2.imshow('Median Blur',median)

# Bilateral Blur
# bilateral = cv2.bilateralFilter(img,35,100,255,10)
# cv2.imshow('Bilateral Blur',bilateral)

cv2.waitKey(0)