# Hand Track

Real-time hand tracking with OpenCV and MediaPipe. `base.py` and `HTrackMod.py` detect and draw hand landmarks from the webcam, and `VolumeControl.py` maps the pinch distance between fingers to the system volume.

## How to run

```
pip install opencv-python mediapipe numpy pycaw comtypes
python base.py
```

## Dependencies

- opencv-python
- mediapipe
- numpy
- pycaw, comtypes (for `VolumeControl.py`)

## Pyodide-runnable

No — it relies on webcam capture, OpenCV GUI windows, MediaPipe, and Windows audio APIs, none of which are available in a browser.
