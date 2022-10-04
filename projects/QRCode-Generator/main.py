# imported library
import qrcode
import qrcode.image.svg as qr

# Accepted the user input
print("Enter the website you need to make QR Code")
s = input()

# QR code box structure
q = qrcode.QRCode(version=1, box_size=10, border=5)

# adding data and fit it.
q.add_data(s)
q.make(fit=True)

# importing as a image and save it in static folder as jpg format
img = q.make_image(fill="black", back_color="white")
img.save("static\qrcode.jpg")
