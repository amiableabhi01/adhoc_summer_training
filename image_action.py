#!/usr/bin/python
import  cv2
import numpy
#  all functions of  cv2  that is opencv model
#print  dir(cv2)

#  reading image
#        image name , imaeg features
#          we can write    cv2.IMREAD_COLOR instead of 1
#          we can write    cv2.IMREAD_BGR2GRAY instead of 0
#          we can write    cv2.IMREAD_UNCHANGE_COLOR instead of -1

img=cv2.imread("car1.jpeg")
#  to draw a line in car image
#        image data , start point , end point , color , line width
cv2.line(img,(0,0),(100,100),(100,120,255),3)
#to draw rectangle
cv2.rectangle(img,(30,20),(300,240),(255,255,255),1)
# to draw circle
cv2.circle(img,(100,100),30,(12,45,200),-1)
#  deciding font type
font=cv2.FONT_HERSHEY_SIMPLEX
#  putting text in image
#           data, text , starting point , fontype , size , color
cv2.putText(img,"CAR",(70,50),font,3,(100,23,200),lineType=cv2.LINE_AA)
# draw polygon over the image of car
vrx = numpy.array(([20,80],[60,50],[100,80],[80,120],[40,120]),numpy.int32)
vrx = vrx.reshape((-1,1,2))
img = cv2.polylines(img, [vrx], True, (0,255,255),3)
cv2.imshow("editedimg",img)
cv2.imwrite("carline.jpeg",img)
cv2.waitKey(0)
