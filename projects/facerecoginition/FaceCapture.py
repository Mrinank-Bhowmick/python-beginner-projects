import cv2

face_classsifier = cv2.CascadeClassifier(
    "haarcascades/haarcascade_frontalface_default.xml"
)


def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classsifier.detectMultiScale(gray, 1.3, 3)
    if faces is ():  # if there is no face
        return None
    print(faces)
    for x, y, w, h in faces:
        cropped_face = img[y : y + h, x : x + w]
        print(cropped_face)
        return cropped_face


# url = 'http://172.20.10.6:8080'
# cam = cv2.VideoCapture(url + '/video')
cam = cv2.VideoCapture(0)
count = 0  # help in counting
while True:
    ret, frame = cam.read()
    if count == 100:
        break
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (300, 300))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        file_name_path = "faces/faces" + str(count) + ".jpg"
        cv2.imwrite(file_name_path, face)
        cv2.putText(
            face, str(count), (70, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2
        )
        cv2.imshow("face crop ", face)
    else:
        print("no face found")
        pass
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
