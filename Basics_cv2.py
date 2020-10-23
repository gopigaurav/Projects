import cv2
import numpy as np
print("package imported")

img = cv2.imread(" Path of the image ")
cv2.imshow("output",img)
cv2.waitKey(1000) # 1000ms second delay

# to capture the video

video = cv2.VideoCapture("Path of the video or give "0" or "1" id to capture the video from the webcam")
video.set(3,640) # id 3 for width set to 640px
video.set(4,480) # id 4 for height set to 780px
video.set(10,100) # id 10 for brightness set to 100


while True:
    success, Video_captured = cap.read()
    cv2.imshow("Video" , Video_captured)

    if cv2.waitkey(1) & 0xFF == ord('q'): # q to quit
        break


#########################################


# in order for the grey scale videos or images

img = cv2.imread("Resources/lena.png")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # color convertion

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # to blur image either color or grey scale

imgCanny = cv2.Canny(img,150,200) # canny images

kernel = np.ones((5,5),np.uint8) # matrix
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)# dilate the edges thicker
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)# erode the images thinner

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)


#######################################################

cv2.imshow("image",img) # to display the shape of the images outputs (wd,ht,color)

# to resize the images
Resize = cv2.resize(img,(1000,500)) # width and height
ptint(Resize.shape)

imgCropped = img[46:119,352:495] # to crop the images

cv2.imshow("Image Cropped",imgCropped) # imshow to show the images



#######################################################

img = np.zeros((512,512,3),np.unit8)
img[:] = 255,0,0 # color for the whole images

img[200:100,100:300] = 255,0,0 # only for the particular points at the edges

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # to draw a line on images

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) # similarly 
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)


cv2.imshow("Image",img)


#######################################################
################## u can wrap the images ##############

width,height = 250,350

pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) # 4 diffrent points of image


pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # 4 coordinates


matrix = cv2.getPerspectiveTransform(pts1,pts2) # 
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)


#########################################################
####################### merging the images ##################

imghor = hp.hstack((img,img)) # horizontal stacking

imgver = np.vstack((img,img)) # vertical stacking

cv2.imshow("Horizontal image stacking" , imghor)
cv2.imshow("vertical image stacking" , imgver)
cv2.waitKey(0)
# above code only works when the both of the color channels are same

###############################################################
####################### merging the more images###########

def stackImages(scale,imgArray):
    
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))

# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
cv2.imshow("ImageStack",imgStack)

cv2.waitKey(0)

##########################################################################

