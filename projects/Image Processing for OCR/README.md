There is 4 steps for building any OCR system.

1. Pre-Processing
    - Pick the region of interest (document)
    - Noise Filtering
    - Skew Correction
    - Convert to Gray Scale
    - Binarize
2. Segmentation
    - Line Segmentation
    - Word Segmentation (optional)
    - Character Segmentation
3. Classification
4. Post-Processing.

Those steps can be broken into more details, but each must be completed to build a complete OCR system. This little project provides with functions that will help with Pre-processing and Segmentation of **printed** characters to build OCR system.

Python packages required for this project-

-   numpy
-   cv2
-   imutils
