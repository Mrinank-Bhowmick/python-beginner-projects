# A pencil shaded image representation with better display of edges
import cv2 as cv
import numpy as np

# Code to read images

img = cv.imread(
    "Photos/image.jpg"
)  # change this path with the path of image passed as an input
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

## Just to check the images obtained in grayscale mode and compare with the original image.
# cv.imshow('image',img)
# cv.imshow('Gray Image', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian Image", lap)

# Sobel Gradient magnitude
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
# cv.imshow('Sobel X',sobelx)
# cv.imshow('Sobel Y',sobely)
cv.imshow("Sobel Final", combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)

cv.waitKey(
    0
)  # keyboard binding function that waits for a specific delay(0 here means to wait for infinite amount of time.)
