# Rubik Tracking

Tracks a green-colored object (e.g., a Rubik's cube) in a live webcam feed using OpenCV color masking and draws its motion trail on screen.

## How to run

```sh
pip install opencv-python imutils numpy
python rubik-tracking.py
```

## Dependencies

- opencv-python
- imutils
- numpy

## Pyodide-runnable

No - it captures live webcam video and shows OpenCV windows, neither of which works in the browser sandbox.
