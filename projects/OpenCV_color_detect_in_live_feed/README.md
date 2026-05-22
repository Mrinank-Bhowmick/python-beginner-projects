# OpenCV Color Detection in Live Feed

Captures a live video feed from a webcam and detects the colour at the centre of the frame. It converts each frame to HSV, reads the hue value at the centre pixel, classifies it into a named colour, and overlays the result on the video.

## Example

1. A window titled "Video" opens showing the live webcam feed.
2. A small green circle marks the centre of the frame.
3. A white rectangle overlays the top-centre area, displaying the detected colour name (e.g. `GREEN`, `BLUE`, `RED`) rendered in the actual BGR colour of the centre pixel.
4. As you move the camera or change what is in the centre, the displayed colour name updates in real time.
5. Press `q` to close the window and stop the feed.

## How to run on localhost

```
pip install opencv-python numpy
python Open_CV_color_detect_in_live_feed.py
```

## Dependencies

- opencv-python
- numpy
