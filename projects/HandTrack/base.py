import cv2
import mediapipe as mp
import time


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
hands = mp_hands.Hands()
while True:
  success, image = cap.read()
  if not success:
    print("Ignoring empty camera frame.")
    continue
  cTime = time.time()
  fps = 1/(cTime - pTime)
  pTime = cTime

  image.flags.writeable = False
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  results = hands.process(image)

  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
      mp_drawing.draw_landmarks(
          image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.DrawingSpec(color=(0,0,256)),
          mp_drawing_styles.DrawingSpec(color=(0, 256, 0)))
  image = cv2.flip(image, 1)
  cv2.putText(image, str(int(fps)), (500,400), cv2.FONT_HERSHEY_PLAIN, 3, (120, 52, 40), 3)
  cv2.imshow('Camera Result', image)
  # print(fps)
  cv2.waitKey(1)