import img2pdf
pdf_data = img2pdf.convert("photo (1).jpg")
file = open("my_pdf.pdf","wb")
file.write(pdf_data)
file.close()
