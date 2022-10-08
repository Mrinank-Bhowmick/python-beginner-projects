import cv2
import time
import numpy as np
import HTrackMod as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


wCam, hCam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(detectionCon=0.7, trackCon=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]

vol = 0
volBar = 400
volP = 0
toggle = 0
while True:
    success, image = cap.read()
    image = detector.findHands(image)
    lmList = detector.finPos(image)
    if not success:
        print('Invalid')
    if len(lmList)!=0:
        # print(lmList[4],lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        x3, y3 = lmList[12][1], lmList[12][2]
        x4, y4 = lmList[20][1], lmList[20][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2


        cv2.circle(image, (x1,y1), 10, (256,0,256),3, cv2.FILLED)
        cv2.circle(image, (x2, y2), 10, (256, 0, 256),3, cv2.FILLED)
        cv2.circle(image, (x3, y3), 10, (256, 0, 256), 3)
        cv2.circle(image, (x4, y4), 10, (256, 0, 256), 3)


        length = math.hypot(x2-x1, y2-y1)
        length2 = math.hypot(x3-x2, y3-y2)
        length3 = math.hypot(x4-x1, y4-y1)
        #Hand: 50-300
        #vol: -65:0
        if length2 < 50:
            toggle ^= 1
        if toggle:
            vol = np.interp(length, [50,200],[minVol, maxVol])
            volBar = np.interp(length, [50, 200], [400, 150])
            volP = np.interp(length, [50, 200], [0, 100])
            # print(vol)
            volume.SetMasterVolumeLevel(vol, None)
            if length < 50:
                cv2.circle(image, (cx, cy), 10, (0, 256, 0), cv2.FILLED)
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(image, (cx, cy), 10, (256, 0, 256), cv2.FILLED)
        if length3 < 30:
            break
        # print(length2)
    image = cv2.flip(image, 1)
    cv2.rectangle(image, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(image, str(int(volP)) + '%', (50, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 3)
        # print(length)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(image, 'fps: ' + str(int(fps)), (500, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (120, 52, 40), 3)
    cv2.imshow('Camera Result', image)

    cv2.waitKey(1)