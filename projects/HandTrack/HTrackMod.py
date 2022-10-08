import cv2
import mediapipe as mp
import time





class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComp=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands=maxHands
        self.modelComp = modelComp
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode,self.maxHands,self.modelComp,self.detectionCon,self.trackCon)

    def findHands(self, image, draw=True):
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                # for id, lm in enumerate(hand_landmarks.landmark):
                #      print(id, lm)
                if draw:
                    self.mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                self.mp_hands.HAND_CONNECTIONS,
                self.mp_drawing_styles.DrawingSpec(color=(0,0,256)),
                self.mp_drawing_styles.DrawingSpec(color=(0, 256, 0)))
        return image
    def finPos(self, image, handNo=0):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand =self.results.multi_hand_landmarks[handNo]


            for id, lm in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
        return lmList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, image = cap.read()
        image = detector.findHands(image)
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        image = cv2.flip(image, 1)
        cv2.putText(image, str(int(fps)), (500,400), cv2.FONT_HERSHEY_PLAIN, 3, (120, 52, 40), 3)
        cv2.imshow('Camera Result', image)
        landmarks = detector.finPos(image)
        if(len(landmarks)!=0):
            print(landmarks[4])
        cv2.waitKey(1)


if __name__ == "__main__":
    main()