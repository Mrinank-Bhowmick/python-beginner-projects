# Mobile Document Scanner

Turns a photo of a document into a clean, top-down "scanned" image. It detects the document edges, finds its contour, applies a four-point perspective transform, and thresholds the result to a black-and-white scan.

## How to run

```
pip install opencv-python numpy imutils scikit-image
python scan.py --image path/to/photo.jpg
```

## Dependencies

- opencv-python
- numpy
- imutils
- scikit-image

## Pyodide-runnable

No — it relies on OpenCV (`cv2`) with `imshow`/`waitKey` GUI windows, which cannot run in a browser.
