# OpenCV Color Detection in Live Feed

Captures a live video feed from a webcam and detects the colour at the centre of the frame. It converts each frame to HSV, reads the hue value at the centre pixel, classifies it into a named colour, and overlays the result on the video.

## How to run

```
pip install opencv-python numpy
python Open_CV_color_detect_in_live_feed.py
```

## Dependencies

- opencv-python
- numpy

## Pyodide-runnable

No — it requires webcam access via OpenCV's `VideoCapture` and `imshow` GUI windows, which are unavailable in the browser.
