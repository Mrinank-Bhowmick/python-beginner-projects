import cv2


img_to_check = input("Input your img: ")


alg_img = cv2.imread(img_to_check)
det_f = cv2.CascadeClassifier('faces.xml')
det_r = det_f.detectMultiScale(alg_img, scaleFactor=2, minNeighbors=3)


if len(det_r) != 0:
    for index, (x, y, w, h) in enumerate(det_r):
        alg_img = alg_img[x:y + h]
        cv2.imwrite(f'images/to_recog/practice/{index}.jpg', alg_img)


cv2.imshow("Result", alg_img)


cv2.waitKey(0)