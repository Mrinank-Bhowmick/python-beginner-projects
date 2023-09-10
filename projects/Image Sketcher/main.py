import cv2
import numpy as np


def sketch(img):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny_edges = cv2.Canny(gray_blur, 10, 70)
    r, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


cap = cv2.VideoCapture(0)
while True:
    r, f = capt.read()
    cv2.imshow("Output", sketch(f))
    if cv2.waitKey(1) == 13:
        break
capt.release()
cv2.destroyAllWindows()
