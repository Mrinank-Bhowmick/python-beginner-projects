#Convert multiple image files in a directory to PDF
import img2pdf
import os

with open("new.pdf","wb") as f:
    f.write(img2pdf.convert([x for x in os.listdir(".") if x.endswith(".png") or x.endswith(".jpg")]))
    f.close()
