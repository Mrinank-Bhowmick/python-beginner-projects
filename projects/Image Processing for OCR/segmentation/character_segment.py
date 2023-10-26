import numpy as np
import cv2


def character_segment(image):
    """
    Segment characters within lines of an image.

    Args:
    - image (ndarray): Preprocessed, Skew Corrected, Binarized input image.

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
        img_line = img[lineStart[count_line]:lineFinish[count_line], 0:col-1]
        
        # Calculate vertical projection
        proj = np.sum(img_line, 0)


        start_temp = []
        finish_temp = []
        count_char = 0
        for i in proj:
            if i != 0 and proj[count_char-1] == 0:
                start_temp.append(count_char)
            elif i == 0 and proj[count_char-1] != 0:
                finish_temp.append(count_char)
            count_char = count_char + 1
        word_start.append(start_temp)
        word_finish.append(finish_temp)
        count_line = count_line + 1

    for x in range(lines):
        for y in range(len(word_start[x])):
            cv2.rectangle(image, (word_start[x][y], lineStart[x]), (word_finish[x][y], lineFinish[x]), (0, 0, 255), 1)
    
    image = cv2.resize(image, (500, 500))
    cv2.imshow(image)

