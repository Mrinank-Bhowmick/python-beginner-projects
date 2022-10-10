import cv2
import numpy as np

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


def empty(a):
	pass
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",300,200)
cv2.createTrackbar("Hue Min","Trackbar",4,179,empty)
cv2.createTrackbar("Hue Max","Trackbar",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbar",226,255,empty)
cv2.createTrackbar("Sat Max","Trackbar",230,255,empty)
cv2.createTrackbar("Val Min","Trackbar",255,255,empty)
cv2.createTrackbar("Val Max","Trackbar",255,255,empty)

while True:
	img = cv2.imread("Extra/color-shapes.png")
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h_min = cv2.getTrackbarPos("Hue Min","Trackbar")
	h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
	s_min = cv2.getTrackbarPos("Sat Min", "Trackbar")
	s_max = cv2.getTrackbarPos("Sat Max", "Trackbar")
	v_min = cv2.getTrackbarPos("Val Min", "Trackbar")
	v_max = cv2.getTrackbarPos("Val Max", "Trackbar")
	# print(h_min,h_max,s_min,s_max,v_min,v_max)
	lower=np.array([h_min,s_min,v_min])
	upper=np.array([h_max,s_max,v_max])
	mask=cv2.inRange(imgHSV,lower,upper)
	imgResult=cv2.bitwise_and(img,img,mask=mask)
	# cv2.imshow("normal",img)
	# cv2.imshow("gray",imgHSV)
	cv2.imshow("mask",mask)
	# cv2.imshow("Result",imgResult)
	# imgREs=np.hstack([img,imgHSV,imgResult])
	# cv2.imshow("stack",imgREs)
	imgfun=stackImages(0.5,([img,imgHSV],[mask,imgResult]))
	cv2.imshow("New",imgfun)
	cv2.waitKey(1)

