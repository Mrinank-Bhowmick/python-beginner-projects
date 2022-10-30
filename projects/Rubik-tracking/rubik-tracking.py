import cv2
import imutils
import numpy as np
from collections import deque
from imutils.video import VideoStream
import argparse
import time

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=50)
args = vars(ap.parse_args())

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])

vs = VideoStream(src=0).start()
time.sleep(2.0)

while 1:
    frame = vs.read()

    frame = imutils.resize(frame, width=700)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)

    pts.appendleft(center)

    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue

        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 4.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 255, 250), thickness)

    cv2.imshow("Rubik's cube tracking", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()
