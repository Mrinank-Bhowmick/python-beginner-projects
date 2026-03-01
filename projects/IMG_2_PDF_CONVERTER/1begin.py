#Convert single image into pdf
import img2pdf
pdf_data = img2pdf.convert("photo (1).jpg")  #Get Image data
file = open("my_pdf.pdf","wb")               #Open or create pdf file
file.write(pdf_data)                         #Write image data to pdf file
file.close()                                 #Close the file
