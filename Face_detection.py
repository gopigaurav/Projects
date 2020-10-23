import cv2

faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml") # open cv package

img = cv2.imread('Resources/lena.png') # image as input  if 1 then color if 0 then grey scale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # u can convert it if u wANT 

faces = faceCascade.detectMultiScale(imgGray,1.1,4,scaleFactor = 1.05) # scale factor to decrease the size of the image by 5% it increases the accuracy

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # to draw a rectangle around the faces that is detected
    

##############################################################

cv2.imshow("Result", img)
cv2.waitKey(0)

video = cv2.VideoCapture(0) # to capture the video from the id 0 or webcam

video.release()
time.sleep(3) # 3s the camera will be on

check,frame=video.read() # to capture the video

print (check)
print(frame)

cv2.imshow("Capturing", frame)
cv2.waitKey(0)
cv2.destroyAllWindows # to destroy all windows 


###########################################################

import cv2,time
video = cv2.VideoCapture(0)

a=1

while true:
    a=a+1
    check,frame = video.read()

    print(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing",gray)

    key = cv2.waitKey(1)
    if key == ord ('q'): # if q is pressed it destroys the window
        break


print(a)
video.release()
cv2.destroyAllWindows
    

############################# feace detection from videos or webcam
import cv2,time
video = cv2.VideoCapture(0)
faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

a=1

while true:
    a=a+1
    check,frame = video.read()

    print(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiscale(gray,1.1,4)
    for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    

    cv2.imshow("Capturing",gray)

    key = cv2.waitKey(1)
    if key == ord ('q'): # if q is pressed it destroys the window
        break


print(a)
video.release()
cv2.destroyAllWindows



















    
