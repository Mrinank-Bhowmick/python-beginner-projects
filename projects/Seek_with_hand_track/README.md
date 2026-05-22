# Seek with Hand Track

Uses a webcam and MediaPipe hand tracking to detect hand gestures and send left/right arrow keypresses, allowing you to seek a video by tilting your hand.

## Example

1. Run `python main.py`. A window titled "MediaPipe Hands" opens showing the live webcam feed.
2. Hold your hand in front of the camera. The script detects hand landmarks and draws circles on the wrist and index-finger base.
3. Tilt your hand so the wrist is to the left of the index finger base (slope < -78°) — a left-arrow keypress is sent and `left` is printed to the console.
4. Tilt your hand in the opposite direction (slope between 0° and 78°) — a right-arrow keypress is sent and `right` is printed.
5. Press Escape to close the window.

## How to run on localhost

```sh
pip install opencv-python mediapipe pyautogui numpy
python main.py
```

## Dependencies

- opencv-python
- mediapipe
- pyautogui
- numpy
