import cv2 as cv
import numpy as np 

cam = cv.VideoCapture(0)
cv.namedWindow('LG-Cam',cv.WINDOW_AUTOSIZE)

x_start = 50
y_start = 50
box_ratio = 0.15
dx = 50
dy = 20

while True:
    resl, frame = cam.read()
    if resl == False:
        print ('There is no Video')
        break
    
    #resize the resolution of the frame
    ratio = 0.6
    new_width = int(frame.shape[1] * ratio)
    new_height = int(frame.shape[0] * ratio)
    dim = (new_width, new_height)
    resized_frame = cv.resize(frame,dim, interpolation = cv.INTER_AREA)
    
    #Bouncing Box
    b_w = int(box_ratio * new_width) #define width of the box
    b_h = int(box_ratio * new_height) # define the height of the box

    cv.rectangle(resized_frame,(x_start,y_start),(x_start + b_w, y_start + b_h),(0,255,0),3 )
    x_start = x_start + dx
    y_start = y_start + dy
    if x_start <= 0 or x_start + b_w > new_width :
        dx = -1 * dx
    if  y_start <= 0 or y_start +b_h >= new_height :
        dy = -1 * dy
        
    cv.imshow('LG-Cam', resized_frame)
    keyEvent = cv.waitKey(1)
    if keyEvent == ord('q'):
        break

cam.release()
cv.destroyAllWindows()

