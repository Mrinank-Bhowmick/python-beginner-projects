# Hand Track

Real-time hand tracking with OpenCV and MediaPipe. `base.py` and `HTrackMod.py` detect and draw hand landmarks from the webcam, and `VolumeControl.py` maps the pinch distance between fingers to the system volume.

## Example

1. Run `python base.py`. A webcam window opens showing the live feed.
2. Hold a hand in front of the camera — MediaPipe detects it and draws 21 landmarks (green dots and connecting lines) over each finger joint.
3. The frame rate (FPS) is printed to the console each second.
4. To control system volume, run `python VolumeControl.py` instead. Pinch your thumb and index finger together to lower the volume; spread them apart to raise it.
5. Press `q` to quit.

## How to run on localhost

```
pip install opencv-python mediapipe numpy pycaw comtypes
python base.py
```

## Dependencies

- opencv-python
- mediapipe
- numpy
- pycaw, comtypes (for `VolumeControl.py`)
