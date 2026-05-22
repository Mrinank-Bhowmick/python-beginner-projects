# Mobile Document Scanner

Turns a photo of a document into a clean, top-down "scanned" image. It detects the document edges, finds its contour, applies a four-point perspective transform, and thresholds the result to a black-and-white scan.

## Example

```text
$ python scan.py --image photo.jpg
STEP 1: Detect the Edges
(two windows open: "Image" showing the resized photo, "Edged" showing Canny edge map — press any key to continue)
STEP 2: Find Contours on paper
(window "Outline" shows the detected document boundary in green — press any key to continue)
STEP 3: Apply perspective transform
(windows "Original" and "Scanned" show the colour photo and the black-and-white top-down scan — press any key to exit)
```

## How to run on localhost

```
pip install opencv-python numpy imutils scikit-image
python scan.py --image path/to/photo.jpg
```

## Dependencies

- opencv-python
- numpy
- imutils
- scikit-image
