# Rubik Tracking

Tracks a green-colored object (e.g., a Rubik's cube) in a live webcam feed using OpenCV color masking and draws its motion trail on screen.

## Example

1. Run `python rubik-tracking.py`. The webcam starts and a window titled "Rubik's cube tracking" opens showing the live feed.
2. Hold a green-colored object (e.g., a green face of a Rubik's cube) in front of the camera. The script detects the green region using HSV color masking and draws a green contour around it.
3. Move the object across the frame. A trailing line is drawn on screen, thicker near the most recent position and thinner further back, tracing the motion path.
4. Press `q` to stop the stream and close the window.

## How to run on localhost

```sh
pip install opencv-python imutils numpy
python rubik-tracking.py
```

## Dependencies

- opencv-python
- imutils
- numpy
