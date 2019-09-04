# Surveilance program. It takes a picture whenever there is motion.
import numpy as np
import cv2
import time
import datetime

font = cv2.FONT_HERSHEY_COMPLEX

cap = cv2.VideoCapture(0)

ret, prev = cap.read()
prev_color = prev.copy()

counter = 0

while True:
    
    ret, frame = cap.read()
    curr_color = frame.copy()

    prev=cv2.medianBlur(prev_color,5)
    curr=cv2.medianBlur(curr_color,5)
    
    diff_color = cv2.subtract(curr_color,prev_color,mask=None)
    diff_color = cv2.medianBlur(diff_color,5)
    diff_gray = cv2.cvtColor(diff_color,cv2.COLOR_BGR2GRAY)
    time.sleep(1)
    frame_copy=frame.copy()
    timestamp = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    cv2.putText(frame_copy,text=timestamp,org=(320,470), fontFace=font,fontScale= 0.5,color=(255,0,255),thickness=1)
    cv2.imshow('Camera view',frame_copy)
    cv2.imshow('Camera burred view',curr)
    cv2.imshow('Difference map',diff_gray)
    cv2.imshow('Difference map color',diff_color)
    
    if 60 < (diff_gray.max()+diff_gray.min())/2:        
        filename = 'detection'+str(counter)+'.jpg'
        counter = counter + 1
        cv2.imwrite(filename,frame_copy)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    prev_color = curr_color

cv2.destroyAllWindows()
cap.release()