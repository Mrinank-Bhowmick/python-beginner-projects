import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

data_path = "faces/"
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

Training_data, Labels = [], []
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
Labels = np.asarray(Labels, dtype=np.int32)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_data), np.asarray(Labels))
print("model traind")

face_classifier = cv2.CascadeClassifier(
    "haarcascades/haarcascade_frontalface_default.xml"
)


def face_detector(img, size=0.5):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(grey, 1.3, 3)
    if faces is ():
        return img, []

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y : y + h, x : x + w]
        roi = cv2.resize(roi, (200, 200))

    return img, roi


url = "http://172.20.10.6:8080"
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(url + '/video')
while True:
    ret, frame = cap.read()

    img, face = face_detector(frame)
    # print(img)
    print(face)
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)
        if result[1] < 500:
            confidence = int(100 * (1 - (result[1]) / 300))
            display_string = str(confidence) + "% confidence"
        cv2.putText(
            img,
            display_string,
            (110, 120),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (250, 120, 255),
        )

        if confidence > 75:
            cv2.putText(
                img, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0)
            )
            cv2.imshow("Face Cropper", img)
        else:
            cv2.putText(
                img, "locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255)
            )
            cv2.imshow("Face Cropper", img)

    except:
        cv2.putText(
            img, "No Face", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255)
        )
        cv2.imshow("Face Cropper", img)
        pass

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
