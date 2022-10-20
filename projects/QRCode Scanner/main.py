import cv2
import numpy as np
from pyzbar.pyzbar import decode


def decoder(image):
    # Creating a black and white style image to avoid confusion
    gray_img = cv2.cvtColor(image, 0)
    # Decoding the gray image to some binary image matrix
    barcode = decode(gray_img)

    # Algorithm to scan the obtained image
    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)

        cv2.putText(
            frame, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2
        )
        print("Barcode: " + barcodeData + " | Type: " + barcodeType)


# Getting user's choice of usage
choice = int(input("1. Scan via image\n2. Scan via WebCam\n Choice: "))
if choice == 2:
    # Accessing webcam for images
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        decoder(frame)
        cv2.imshow("Image", frame)
        code = cv2.waitKey(10)
        if code == ord("q"):
            break
else:
    # Scanning the qrcode in locally available image
    img_path = input("Enter Image path: ")
    img = cv2.imread(img_path)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    print("QRCode Encoded Data: ", data)
