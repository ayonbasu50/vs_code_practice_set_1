#pylint:disable=no-member

import cv2 as cv

def rescaleFrame(frame, scale = 0.7): # this function works for images , video and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# # Reading Images

# img = cv.imread('C:/Users/ayonb/VS_Code_practice/opencv-course-master/Resources/Photos/cat_large.jpg')
# resized_img = rescaleFrame(img)
# cv.imshow('Resized Cat', resized_img)

# cv.waitKey(0)

# # Reading Videos
# def changeRes(weight,height): # this function works for live video only
#     capture.set(3,width)
#     capture.set(4,height)

capture = cv.VideoCapture('opencv-course-master\Resources\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()