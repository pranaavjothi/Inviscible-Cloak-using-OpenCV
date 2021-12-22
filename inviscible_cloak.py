import cv2
import numpy as np
cap=cv2.VideoCapture(0)
_,fr=cap.read(10)
while(1):
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40,40,40])
    upper_green = np.array([80,255,255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    color_mask = cv2.bitwise_and(fr,fr,mask=mask)
    n1=cv2.bitwise_not(mask)
    n2=cv2.bitwise_and(frame,frame,mask=n1)
    added=cv2.add(color_mask,n2)
    cv2.imshow('Original',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('ColourMask',color_mask)
    cv2.imshow('final',added)
    k = cv2.waitKey(5) & 0xFF                                   
    if k == 27:                                                 
        break                                                   
cv2.destroyAllWindows()                                         
cap.release()
