# Face Recognition

A two-part OpenCV face recognition demo. `FaceCapture.py` captures face crops from your webcam and saves them; `FaceDetection.py` trains an LBPH recognizer on those crops and live-detects faces, displaying an "Unlocked"/"locked" overlay based on confidence.

## How to run

```
pip install opencv-contrib-python numpy
python FaceCapture.py
python FaceDetection.py
```

## Dependencies

- opencv-contrib-python
- numpy

## Pyodide-runnable

No — it relies on OpenCV webcam capture (`cv2.VideoCapture`) and GUI windows, which are not available in a browser.
