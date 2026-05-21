# Seek with Hand Track

Uses a webcam and MediaPipe hand tracking to detect hand gestures and send left/right arrow keypresses, allowing you to seek a video by tilting your hand.

## How to run

```sh
pip install opencv-python mediapipe pyautogui numpy
python main.py
```

## Dependencies

- opencv-python
- mediapipe
- pyautogui
- numpy

## Pyodide-runnable

No - it captures live webcam video, runs MediaPipe, and simulates keypresses with `pyautogui`, none of which work in the browser sandbox.
