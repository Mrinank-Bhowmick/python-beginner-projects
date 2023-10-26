import numpy as np
import cv2

def skew_correct(image):
    """
    Correct skew in an image.

    Args:
    - image (ndarray): The input image (grayscale and inverted).

    Returns:
    - ndarray: The deskewed image.
    """
    # Find the coordinates of all pixel values greater than zero
    coords = np.column_stack(np.where(image > 0))

    # Compute the angle of the minimum area rectangle that contains the coordinates
    angle = cv2.minAreaRect(coords)[-1]

    # Adjust the angle to the range (-45, 45) degrees
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    # Get image dimensions
    (h, w) = image.shape[:2]

    # Calculate the rotation center
    center = (w // 2, h // 2)

    # Create a rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Rotate the image to deskew it
    rotated_img = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated_img
