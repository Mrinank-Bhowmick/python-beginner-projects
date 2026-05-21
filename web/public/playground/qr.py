# QR Code Generator
# Turns any text or URL into a QR code drawn right in the terminal.

import qrcode

text = input("Enter text or a URL to encode: ")

qr = qrcode.QRCode(border=2)
qr.add_data(text)
qr.make(fit=True)

print()
print(f"QR code for: {text}")
print()
qr.print_ascii()
