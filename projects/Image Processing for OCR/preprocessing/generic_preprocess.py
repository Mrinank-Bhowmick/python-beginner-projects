def preprocess_img(image, kernel_size=9, skip_dilatation=False):
    """
    Preprocess an image for better results in OCR by applying Gaussian blur, adaptive thresholding, and dilation.

    Args:
    - img (ndarray): The input image to be preprocessed.
    - kernel_size (int, optional): The size of the Gaussian blur kernel.
    - skip_dilatation (bool, optional): Whether to skip the dilation step.

    Returns:
    - ndarray: The preprocessed image.
    """
    if len(image.shape) != 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    noise_reduced_img = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Apply adaptive thresholding to binarize the image
    binarized_img = cv2.adaptiveThreshold(noise_reduced_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Invert colors to emphasize gridlines (non-zero pixels)
    inverted_img = cv2.bitwise_not(binarized_img, binarized_img)

    if not skip_dilatation:
        # Apply dilation to make gridlines more pronounced
        kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
        return cv2.dilate(inverted_img, kernel)

    return inverted_img
