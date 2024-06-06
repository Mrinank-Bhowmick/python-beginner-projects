import cv2
import numpy as np


def image_to_sketch(image_path):
    img = cv2.imread(image_path)
    # converting to gray scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # applying gaussian blur
    blurred_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
    inverted_blurred_img = cv2.bitwise_not(blurred_img)
    sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)
    cv2.imshow("Pencil Sketch", sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # save the results
    output_file_name = "sketch_of" + "" + image_path
    output = cv2.imwrite(output_file_name, sketch_img)
    print(f"Saved the Sketch!")
    return output


if __name__ == "__main__":
    image = "# your image"
    image_to_sketch(image)
