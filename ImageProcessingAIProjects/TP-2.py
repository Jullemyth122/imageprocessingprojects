# This is for resizing the images 
import cv2 as cv


# For Images, Live, Video
def resizeFrame(frame,scale=0.5):
    print(frame.shape)
    width = int(frame.shape[1] * scale);
    height = int(frame.shape[0] * scale);
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# For Live Video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
    return capture
# Resize Images
# img = cv.imread('C:/PythonAlgorithm/ImageProcessingAIProjects/Photos/1.png')
# img = cv.cvtColor(img,cv.COLOR_BGR2BGRA)
# resizeImg = resizeFrame(img)
# cv.imshow('Cat',resizeImg)

# Resize Video
# capture = cv.VideoCapture("C:/PythonAlgorithm/ImageProcessingAIProjects/Vidoes/paradise.mp4")
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    # print(isTrue,frame)

    resizeVid = resizeFrame(frame)
    cv.imshow("Video",frame) 
    cv.imshow("Video2",resizeVid) 

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()           
cv.waitKey(0)