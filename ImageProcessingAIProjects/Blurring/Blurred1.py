import cv2
import numpy as np

# img = cv2.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
# img = cv2.resize(img, (700, 700))

# # Create a mask for the object of interest
# mask = np.zeros(img.shape[:2], dtype=np.uint8)
# mask[200:500, 200:500] = 255

# # Apply a blur to the object of interest
# blur = cv2.blur(img, (50,50),(250,250))

# # Show the original image
# cv2.imshow('Original', img)

# # Show the image with the blur applied to the object of interest
# cv2.imshow('Blur', blur)
# cv2.imshow('mask', mask)
# cv2.waitKey(0)

img = cv2.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
img = cv2.resize(img,(700,700),interpolation=cv2.INTER_CUBIC)

# Create a binary mask with the same shape as the image
mask = np.zeros_like(img)
mask[200:500,200:500] = 255

# Apply the mask to the image
img2 = img
img = cv2.bitwise_and(img, mask)

# Apply blur with anchor point
blurred_img = cv2.blur(img,(25,25),(1,250))
blurred_img2 = cv2.blur(img2,(25,25),(1,250))

cv2.imshow('Original Image1',img)
cv2.imshow('Original Image2',img2)
cv2.imshow('Blurred Image with mask',blurred_img)
cv2.imshow('Blurred Image with mask2',blurred_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()