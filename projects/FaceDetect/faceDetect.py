import argparse
import cv2

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", type = str, required = True, help = "Path to input image")
arg.add_argument("-c", "--cascade", type = str, required = True, help = "Path to haarcascade file")
args = vars(arg.parse_args())

detector = cv2.CascadeClassifier(args["cascade"])

image = cv2.imread(args["image"])
resizeImage = cv2.resize(image, (500,500))
gray = cv2.cvtColor(resizeImage, cv2.COLOR_BGR2GRAY)
rect = detector.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5,
                                 minSize = (0,0), maxSize=(300,300))
for (x, y, w, h) in rect:
    cv2.rectangle(resizeImage, (x,y),(x+w, y+h), (0,255,0), 2)

cv2.imshow("Image", resizeImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
