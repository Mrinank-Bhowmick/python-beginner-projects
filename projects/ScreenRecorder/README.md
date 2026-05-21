# Screen Recorder using Python

### First install this modules by enter this lines in your terminal

pip install opencv-python

pip install pywin32

pip install numpy

pip install pyautogui

# Now run the main.py 

## Great.............You Did it, Check your folder and find "ScreenRecord.mp4" file

## Dependencies

- opencv-python
- pywin32
- numpy
- pyautogui

## Pyodide-runnable

No - it captures the real screen with `pyautogui` and uses Windows-specific `win32api`, neither of which works in the browser sandbox.
