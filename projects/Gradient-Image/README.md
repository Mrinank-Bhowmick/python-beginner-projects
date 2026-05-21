# Gradient Image

An OpenCV demo that loads an image and displays edge-detection results — Laplacian, combined Sobel gradient, and Canny — in separate windows for a pencil-shaded style representation.

## How to run

```
pip install opencv-python numpy
python gradient.py
```

## Dependencies

- opencv-python
- numpy

## Pyodide-runnable

No — it uses OpenCV GUI windows (`cv.imshow`), which are not available in a browser.
