# Gradient Image

An OpenCV demo that loads an image and displays edge-detection results — Laplacian, combined Sobel gradient, and Canny — in separate windows for a pencil-shaded style representation.

## Example

1. Place an image at `Photos/image.jpg` and run `python gradient.py`.
2. Three windows open side by side:
   - **Laplacian Image** — highlights rapid intensity changes as bright edges on a black background.
   - **Sobel Final** — shows combined horizontal and vertical gradient magnitude.
   - **Canny** — clean single-pixel edge outlines using Canny detection (thresholds 150–175).
3. Press any key to close all windows.

## How to run on localhost

```
pip install opencv-python numpy
python gradient.py
```

## Dependencies

- opencv-python
- numpy
