import cv2,time
import numpy as np

face_Cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
a=1

video = cv2.VideoCapture(0)
while True:
    a=a+1
    check,frame = video.read()

    print(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_Cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = frame[y:y+h , x:x+w]
        eye = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in faces:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                                    
            
                                    
    

    cv2.imshow("Capturing",frame)

    key = cv2.waitKey(1)
    if key == ord ('q'): # if q is pressed it destroys the window
        break


print(a)
video.release()
cv2.destroyAllWindows
