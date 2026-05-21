# QRCode Scanner
**An app to scan QRcode via image or Webcam available in PC.**

### Tools/FrameWorks used:
 - pyzbar
 - opencv-python
 - numpy

## Installation
Simple, Just clone this repository to your local storage and run the below command.
` pip install -r requirements.txt `

## Execution
Run the below command in command prompt or terminal.
`python3 main.py`

## Dependencies

- opencv-python
- numpy
- pyzbar

## Pyodide-runnable

No - it uses OpenCV (`cv2.imshow`, webcam capture) and `pyzbar`, none of which are available in the browser sandbox.
