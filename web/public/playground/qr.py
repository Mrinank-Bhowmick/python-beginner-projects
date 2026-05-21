# === QRCode Generator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @SubramanyaKS.

import qrcode

# Ask user for text or URL to encode
text = input("Enter text or a URL to encode: ")

# Build the QR code object
qr = qrcode.QRCode(border=2)
qr.add_data(text)
qr.make(fit=True)

# Print the QR code as ASCII art
print()
print(f"QR code for: {text}")
print()
qr.print_ascii()
