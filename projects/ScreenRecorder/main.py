# First of all import this modules

import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as nu
import time

# Then set width and height of your recorder same as your screen

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension = (width, height)


format = cv2.VideoWriter_fourcc(*"XVID")

# Here you can change the FPS (Frame Per Second)

video_output = cv2.VideoWriter("ScreenRecord.mp4", format, 30.0, dimension)

# Set the time interval of Recording
# Take how much time you required in the Duration variable

Present_time = time.time()
Duration = 10
finish_time = Present_time + Duration

while True:
    #   Here pyautogui.screenshot() captured screenshots which merge into a ScreenRecord
    picture = pyautogui.screenshot()
    # Here we store all the screenshots in an array
    frame = nu.array(picture)
    # Here we get the original color by using cv2.COLOR_BGR2RGB
    frame_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Now we store the video output here
    video_output.write(frame_1)
    # Now check the duration
    current_time = time.time()
    if current_time > finish_time:
        break
# Finally release your ScreenRecord
video_output.release()

print("____Screen Recording finished________")
