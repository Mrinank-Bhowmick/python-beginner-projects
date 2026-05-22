# QR Code Generator with Window and Simple UI

A Tkinter desktop application that takes a text/URL, save location, file name, and size, then generates a QR code image and saves it to the chosen directory.

## Example

1. The window titled "RavenyBoi's QR code generator" opens with four input fields: text/URL, save location, file name, and size (1–40).
2. Enter `https://github.com` in "Enter the text/URL", `C:\Users\Alice\Desktop` in the location field, `my_qr` as the file name, and `5` as the size.
3. Click "Generate Code". A QR code image is saved to `C:\Users\Alice\Desktop\my_qr.png` and a pop-up confirms "QR Code is saved successfully!".

## How to run on localhost

```sh
pip install qrcode pillow
python main.py
```

## Dependencies

- qrcode
- pillow
- tkinter (standard library)
