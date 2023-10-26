import numpy as np
import cv2

def otsu_thresh(image):
    """
    Apply Otsu's thresholding to an input image.

    Args:
    - image (ndarray): The input grayscale image.

    Returns:
    - int: The computed Otsu threshold value.
    - ndarray: The thresholded binary image.
    """
    # Compute the histogram of the input image
    hist, bin_edges = np.histogram(image, bins=256)
    
    # Normalize the histogram
    hist = np.divide(hist.ravel(), hist.max())
    
    # Compute bin centers
    bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.
    
    # Calculate cumulative weights and means
    weight1 = np.cumsum(hist)
    weight2 = np.cumsum(hist[::-1])[::-1]
    mean1 = np.cumsum(hist * bin_mids) / weight1
    mean2 = (np.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]
    
    # Compute inter-class variance
    inter_class_variance = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2
    
    # Find the index of the maximum inter-class variance
    index_of_max_val = np.argmax(inter_class_variance)
    
    # Determine the threshold value
    threshold = bin_mids[:-1][index_of_max_val]
    
    # Slightly adjust the threshold for practical use
    threshold = int(1.1 * threshold)
    
    # Apply Otsu's thresholding to the image
    image_result = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    return threshold, image_result
