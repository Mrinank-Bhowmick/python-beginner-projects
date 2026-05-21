# QR Code Generator with Window and Simple UI

A Tkinter desktop application that takes a text/URL, save location, file name, and size, then generates a QR code image and saves it to the chosen directory.

## How to run

```sh
pip install qrcode pillow
python main.py
```

## Dependencies

- qrcode
- pillow
- tkinter (standard library)

## Pyodide-runnable

No - it builds a Tkinter GUI and writes image files to real disk paths, neither of which works in the browser sandbox.
