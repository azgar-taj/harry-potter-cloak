import numpy as np
import cv2

cap = cv2.VideoCapture(0)
img = cv2.imread("C:\\path\\pcimg1.jpg")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_o = frame
    lower_red = np.array([90,150,0])
    upper_red = np.array([120,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(img,img, mask= mask)
    mask = cv2.bitwise_not(mask)
    frame = cv2.bitwise_and(frame,frame,mask = mask)
    conx = res + frame
    # Display the resulting frame
    #cv2.imshow('frame',frame)
    #cv2.imshow('res',res)
    cv2.imshow('frame_o',conx)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()