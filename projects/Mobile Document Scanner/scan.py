# importing the necessary libraries
from transform import four_point_transform
from skimage.filters import threshold_local

# this will help us to obtain black and white feel to our scanned image
import numpy as np
import argparse
import cv2
import imutils

# constructing the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image to be scanned")
args = vars(ap.parse_args())

# Step 1: Edge Detection

# load the image and compute the ratio of the old height to the new height, clone it, resize it
image = cv2.imread(args["image"])
ratio = image.shape[0] / 500.0
# ratio of original height to the new height
orig = image.copy()
image = imutils.resize(image, height=500)
# we are setting our scanned image to have a height of 500 pixels
# convert the image to grayscale and blur it and find the edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
# gaussian blur to remove high frequency noise

edged = cv2.Canny(gray, 75, 200)

# show the original image and the edge detected one
print("STEP 1: Detect the Edges")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Finding Contours
# find the contours on the edged image, keeping only the largest ones
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

# loop over all the contours
for c in cnts:
    # approx the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # if the approximated contour has 4 points, we found our screen
    if len(approx) == 4:
        screenCnt = approx
        break


# show the contour
print("STEP 2: Find Contours on paper")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Apply a perspective transform and threshold
# apply the four point transform to obtain top down view

warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

# convert it to grayscale, then threshold it
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset=10, method="gaussian")
warped = (warped > T).astype("uint8") * 255

# show
print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height=650))
cv2.imshow("Scanned", imutils.resize(warped, height=650))
cv2.waitKey(0)
