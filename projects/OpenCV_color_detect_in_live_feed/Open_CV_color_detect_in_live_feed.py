import cv2
import numpy as np

cap = cv2.VideoCapture(
    0
)  # This allows the opencv to access your webcam, you can change it from 0 to any integer 1 or 2 if you are using another webcam or camera
cap.set(3, 1080)
cap.set(4, 720)
cap.set(10, 100)

while (
    True
):  # we are using a loop, because we get a stream of images called frames and by using loop we can convert them into continuous stream i.e. video
    success, img = cap.read()
    hsv_img = cv2.cvtColor(
        img, cv2.COLOR_BGR2HSV
    )  # converting the image captured from rgb format to hsv format as it is easier to do color detection on it
    height, width, _ = img.shape

    cx = int(width / 2)
    cy = int(height / 2)
    cv2.circle(img, (cx, cy), 10, (0, 255, 0), 2)

    pixel_center_bgr = img[cy, cx]
    pixel_center = hsv_img[cy, cx]
    hue_val = pixel_center[0]

    color = "Undefined"  # below loops gives an output of detected color based on the hue value range
    if hue_val < 5:
        color = "RED"
    elif hue_val < 22:
        color = "ORANGE"
    elif hue_val < 33:
        color = "YELLOW"
    elif hue_val < 78:
        color = "GREEN"
    elif hue_val < 131:
        color = "BLUE"
    elif hue_val < 170:
        color = "VIOLET"
    elif hue_val < 180:
        color = "BLACK"
    else:
        color = "RED"

    b, g, r = (
        int(pixel_center_bgr[0]),
        int(pixel_center_bgr[1]),
        int(pixel_center_bgr[2]),
    )  # 3 lines here determine the UI element of cv2 frame
    cv2.rectangle(img, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(img, color, (cx - 200, 100), 0, 3, (b, g, r), 5)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord(
        "q"
    ):  # this lines tells opencv to exit out of while loop when q is pressed
        break

cap.release()
cv2.destroyAllWindows()
