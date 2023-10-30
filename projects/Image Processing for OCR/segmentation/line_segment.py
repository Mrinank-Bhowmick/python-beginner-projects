import numpy as np
import cv2

def line_segment(image, width = 500):
    """
    Perform line segmentation on a preprocessed, inverted, and deskewed image.

    Args:
    - image (ndarray): Preprocessed, Skew Corrected, Binarized input image.
    - width (int, optional): The desired width for the output histogram image.

    Returns:
    - list: Lists of line starting and finishing positions.
    """
    # Calculate horizontal projection
    proj = np.sum(image, 1)

    # Create an output image with the same height as the text and the specified width
    m = np.max(proj)
    histogram_result = np.zeros((proj.shape[0], width))  

    # Draw a line for each row in histogram
    for row in range(image.shape[0]):
        cv2.line(histogram_result, (0, row), (int(proj[row] * width / m), row), (255, 255, 255), 1)
    
    j = 0
    count = 0
    line_start = []
    line_finish = []
    for i in proj:
        if i != 0 and j == 0:
            line_start.append(count)
        elif i == 0 and j != 0:
            line_finish.append(count)
        j = i
        count = count + 1
    count = 0

    view_result(image.copy(), line_start, line_finish)

    return line_start, line_finish


def view_result(image, line_start, line_finish):
    """
    Visualize the line segmentation result.

    Args:
    - image (ndarray): The original image.
    - histogram_result (ndarray): The histogram result image.
    - line_start (list): Lists of line starting positions.
    - line_finish (list): Lists of line finishing positions.
    """
    col = image.shape[1]

    for count in range(len(line_start)):
        cv2.line(image, (0, line_start[count]), (col - 1, line_start[count]), (255, 255, 255), 1)
        cv2.line(image, (0, line_finish[count]), (col - 1, line_finish[count]), (255, 255, 255), 1)

    image = cv2.resize(image, (500, 500))
    cv2.imshow(image)