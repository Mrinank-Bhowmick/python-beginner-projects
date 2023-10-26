import numpy as np
import cv2
import imutils
from skimage.filters import threshold_local


def order_points(pts):
    """
    Order a list of four points to determine their arrangement in a consistent order (top-left, top-right, bottom-right, bottom-left).

    Args:
    - pts (ndarray): A list of four points with inconsistent ordering.

    Returns:
    - ndarray: An ordered list of four points with a consistent arrangement.
    """
    rect = np.zeros((4, 2), dtype="float32")
    # top-left point = smallest sum of (X+Y)
    # bottom-right = largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    
    # top-right point = smallest difference (X-Y)
    # bottom-left = largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def four_point_transform(image, pts):
    """
    Apply perspective transform to an image using four specified points to get a top down view of original image.

    Args:
    - image (ndarray): The input image.
    - pts (ndarray): A list of four points defining the region of interest (ROI).

    Returns:
    - ndarray: The top-down view of the original image after perspective transformation.
    """
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # width of the new image will be the maximum distance
    # between bottom-right and bottom-left x-coordinates 
    # or the top-right and top-left x-coordinates
    width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    max_width = max(int(width_a), int(width_b))

    # height of the new image will be the maximum distance
    # between the top-right and bottom-right y-coordinates 
    # or the top-left and bottom-left y-coordinates
    height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    max_height = max(int(height_a), int(height_b))

    # construct the set of destination points to obtain the top-down view of the image,
    # again specifying points in the top-left(0,0) , top-right, bottom-right, and bottom-left order(0, maxHeight - 1)
    dst = np.array([[0, 0], [max_width - 1, 0], [max_width - 1, max_height - 1], [0, max_height - 1]], dtype="float32")
    
    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (max_width, max_height))
    
    return warped

# the image needs to be preprocessed
def crop_func(image, default_height = 500, view_size = 700):
    """
    Crop a document from an image, apply perspective transform, and threshold the image. 
    Works only when the document area is separable from outside via edge and contrast and is the largest.

    Args:
    - image (ndarray): The preprocessed input image containing the document.
    - default_height (int, optional): The default height for resizing.
    - view_size (int, optional): The desired size for the output image.

    Returns:
    - ndarray: The cropped, transformed, and thresholded document image.
    """
    ratio = image.shape[0] / default_height
    orig = image.copy()
    image = imutils.resize(image, height= default_height)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 75, 250)


    # find the contours in the edged image, keeping only the largest ones, and initialize the screen contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if the approximated contour has four points, that is assumed as the document
        if len(approx) == 4:
            screen_cnt = approx
            break
    # Finding contours of paper
    cv2.drawContours(image, [screen_cnt], -1, (0, 255, 0), 2)
    # cv2.imshow("Outline", image)

    # the four point transform lets us obtain a top-down view of the original image
    warped = four_point_transform(orig, screen_cnt.reshape(4, 2) * ratio)
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped, 11, offset=10, method="gaussian")
    warped = (warped > T).astype("uint8") * 255
    #resize
    warped = imutils.resize(warped, height = view_size//2)


    # To show the original and scanned images 
    # Apply perspective transform
    orig = imutils.resize(orig, height = view_size//2)
    # view_result(warped, orig, view_size)
    return warped

def view_result(warped, orig, view_size,):
    warped = cv2.resize(warped, (view_size, view_size))
    orig = cv2.resize(orig, (view_size, view_size)) 
    image_array = ([orig, warped])
    img_stacked = image_stack(image_array, 0.5)
    cv2.imshow(img_stacked)