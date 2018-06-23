#!/usr/bin/python
import cv2
#loading image
img=cv2.imread('car1.jpeg')
img1=cv2.imread('car1.jpeg',0)
#print height and width
print img.shape
#to display that image
cv2.imshow("car",img)
cv2.imshow("carnew",img1)

# image window holder activate
cv2.waitKey(0)
#waitkey will destroy by using q button
cv2.destroyAllwindows()
