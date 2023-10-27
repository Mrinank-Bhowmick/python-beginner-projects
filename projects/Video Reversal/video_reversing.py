import cv2

cap = cv2.VideoCapture("sampleVideo.mp4")

frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

print("No. of frames: {}".format(frames))
print("FPS: {}".format(fps))

idx = frames - 1

if cap.isOpened():
    while idx != 0:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        frame = cv2.resize(frame, (int(width), int(height)))
        idx -= 1
        if idx % 100 == 0:  # printing progress
            print(idx)
        cv2.imshow("reversed", frame)  # displaying the output
        cv2.waitKey(10)
cap.release()
cv2.destroyAllWindows()
