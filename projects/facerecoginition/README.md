# Face Recognition

A two-part OpenCV face recognition demo. `FaceCapture.py` captures face crops from your webcam and saves them; `FaceDetection.py` trains an LBPH recognizer on those crops and live-detects faces, displaying an "Unlocked"/"locked" overlay based on confidence.

## Example

1. Run `FaceCapture.py`. A webcam window titled "face crop" opens and begins capturing your face.
2. The script saves up to 100 grayscale face crops as `faces/faces1.jpg`, `faces/faces2.jpg`, etc. and prints the bounding-box coordinates for each detected face.
3. If no face is detected in a frame, it prints `no face found` and waits for the next frame.
4. Run `FaceDetection.py`. It trains the LBPH recognizer on the saved crops and opens a live webcam feed.
5. Recognised faces show an "Unlocked" overlay; unrecognised faces show "locked".

## How to run on localhost

```
pip install opencv-contrib-python numpy
python FaceCapture.py
python FaceDetection.py
```

## Dependencies

- opencv-contrib-python
- numpy
