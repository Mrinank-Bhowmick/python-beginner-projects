import numpy as np
import cv2


def character_segment(image, line_start, line_finish, threshold_factor = 20):
    """
    Segment characters within lines of an image.

    Args:
    - image (ndarray): Preprocessed, Skew Corrected, Binarized input image.
    - line_start, line_finish : points obtained from line segmentation
    - threshold: default is 20, 
    if you experience under-segmentation(not all characters separated), increase the value
    otherwise (under-segmentation), decrease it

    Note:
    - This function assumes that you have preprocessed the image and obtained line starting and finishing positions
      using the `lineStart` and `lineFinish` variables.

    Returns:
    - None: This function displays the image with character boundaries drawn.
    """
    count_line = 0
    word_start = []
    word_finish = []
    lines = len(lineStart)
    col = image.shape[1]

    for x in range(lines):
        img_line = image[line_start[count_line]:line_finish[count_line], 0:col-1]
        
        # Calculate vertical projection
        proj = np.sum(img_line, 0)


        start_temp = []
        finish_temp = []
        count_char = 0
        threshold = np.max(proj) // threshold_factor
        for i in proj:
            if i > threshold and proj[count_char-1] <= threshold:
                start_temp.append(count_char)
            elif i <= threshold and proj[count_char-1] > threshold:
                finish_temp.append(count_char)
            count_char = count_char + 1
        word_start.append(start_temp)
        word_finish.append(finish_temp)
        count_line = count_line + 1

    for x in range(lines):
        for y in range(len(word_start[x])):
            cv2.rectangle(image, (word_start[x][y], line_start[x]), (word_finish[x][y], line_finish[x]), (255, 255, 255), 1)
     
    image = cv2.resize(image, (500, 500))
    cv2.imshow(image)

