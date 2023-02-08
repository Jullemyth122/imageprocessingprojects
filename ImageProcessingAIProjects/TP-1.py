# This file is to read the OpenCV configuration
import cv2 as cv

# For reading image and show
# img = cv.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
# img = cv.cvtColor(img,cv.COLOR_BGR2BGRA)
# cv.imshow('Cat',img)
# cv.waitKey(0)

# For reading videos
# Input "0" for capturing camera-real-time
# Input "path/to/video" for opening video file
capture = cv.VideoCapture("C:/PythonAlgorithm/ImageProcessingAIProjects/Vidoes/paradise.mp4")

while True:
    isTrue, frame = capture.read()
    print(isTrue,frame)

    cv.imshow("Video",frame) 

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()           
cv.waitKey(0)

