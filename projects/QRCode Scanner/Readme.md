# QRCode Scanner
**An app to scan QRcode via image or Webcam available in PC.**

### Tools/FrameWorks used:
 - pyzbar
 - opencv-python
 - numpy

## Example

**Scan from an image file:**
```text
1. Scan via image
2. Scan via WebCam
 Choice: 1
Enter Image path: sample_qr.png
QRCode Encoded Data:  https://example.com
```

**Scan via webcam:**
```text
1. Scan via image
2. Scan via WebCam
 Choice: 2
```
A live webcam window opens. When a QR code comes into frame, a green polygon is drawn around it and the decoded text is printed:
```text
Barcode: https://example.com | Type: QRCODE
```
Press `q` to close the window.

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
