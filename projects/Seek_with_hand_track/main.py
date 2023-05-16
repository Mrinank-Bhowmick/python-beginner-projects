import cv2
import mediapipe as mp
import pyautogui as pa
import time
import numpy as np

# Easy module names
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def get_coord(landmrk, image_width, image_height):
    """
    converts relative coordinates to pixel coordinates
    """
    return int(landmrk.x * image_width), int(landmrk.y * image_height)


# Measure time
# this is required to  execute process_inp after every n milliseconds
_time = time.time()


def process_inp(k, l):
    ## Detect clockwise anticlockwise
    global _time
    # print(time.time() - _time )

    # only detect input every 500 ms
    if time.time() - _time > 0.5:
        _time = time.time()

        # reject hand if it is far away
        if l > 0.2:
            if k < -78:
                print("left")
                pa.press("left")
            elif k < 78 and k > 0:
                print("right")
                pa.press("right")


# For webcam input:
cap = cv2.VideoCapture(0)


with mp_hands.Hands(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5
) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        image_height, image_width, _ = image.shape

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Here is How to Get All the Coordinates

                landmrk1 = hand_landmarks.landmark[0]
                x1, y1 = get_coord(landmrk1, image_width, image_height)
                image = cv2.circle(
                    image, (int(x1), int(y1)), 20, (255, 0, 0), thickness=2
                )

                landmrk2 = hand_landmarks.landmark[5]
                x2, y2 = get_coord(landmrk2, image_width, image_height)
                image = cv2.circle(
                    image, (int(x2), int(y2)), 20, (255, 0, 0), thickness=2
                )

                slope = np.degrees(
                    np.arctan((landmrk1.y - landmrk2.y) / (landmrk1.x - landmrk2.x))
                )
                l = np.sqrt(
                    (landmrk1.x - landmrk2.x) ** 2 + (landmrk1.y - landmrk2.y) ** 2
                )
                print(slope, l)
                process_inp(slope, l)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow("MediaPipe Hands", cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
