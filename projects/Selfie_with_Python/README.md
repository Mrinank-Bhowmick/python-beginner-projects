# Selfie with Python

Opens the webcam in an OpenCV window; press Space to capture a selfie (saved as a JPG) and Escape to quit.

## Example

```text
Press Space-bar to click Selfie
Press Escape key to terminate the window
```

1. A window titled "Take selfie with python" opens showing the live webcam feed.
2. Press Space to capture a photo — `Selfie_0.jpg` is saved in the current directory and `Selfie taken!` is printed.
3. Press Space again to save `Selfie_1.jpg`, and so on.
4. Press Escape to close the window — `Escape hit, closing the window` is printed.

## How to run on localhost

```sh
pip install opencv-python
python Selfie_with_Python.py
```

## Dependencies

- opencv-python
- time (standard library)
