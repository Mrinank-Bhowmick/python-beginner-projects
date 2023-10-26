import numpy as np
import cv2

def image_stack(img_array, scale, labels=[]):
    """
    Stack a list of images horizontally and add labels.

    Args:
    - img_array (list of lists or list of ndarrays): A list of images to stack. It can be a list of lists
      for stacking multiple rows of images.
    - scale (float): The scaling factor for resizing the images.
    - labels (list of lists, optional): Labels for the images. It should have the same structure as img_array.

    Returns:
    - ndarray: The horizontally stacked and labeled image.

    Note:
    - The input images should be in the form of NumPy ndarrays.
    - If labels are provided, they are displayed above each image in the stack.
    """

    rows = len(img_array)
    cols = len(img_array[0])

    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]

    if isinstance(img_array[0], list):
        for x in range(0, rows):
            for y in range(0, cols):
                img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        img_blank = np.zeros((height, width, 3), np.uint8)
        hor = [img_blank] * rows
        hor_con = [img_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
            hor_con[x] = np.concatenate(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(rows):
            img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor

    if labels:
        each_img_width = int(ver.shape[1] / cols)
        each_img_height = int(ver.shape[0] / rows)
        for d in range(rows):
            for c in range(cols):
                cv2.rectangle(ver, (c * each_img_width, each_img_height * d),
                              (c * each_img_width + len(labels[d][c]) * 13 + 27, 30 + each_img_height * d), (255, 255, 255),
                              cv2.FILLED)
                cv2.putText(ver, labels[d][c], (c * each_img_width + 10, each_img_height * d), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (255, 0, 255), 2)
    return ver
