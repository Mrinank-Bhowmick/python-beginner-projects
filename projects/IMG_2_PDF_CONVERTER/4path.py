import img2pdf
import os

path0 = os.getcwd()
path1 = r'C:\Users\Dell\Desktop\photos'
os.chdir(path1)
list = os.listdir(".")
newList = [x for x in list if x.endswith(".png") or x.endswith(".jpg")]
print("total no of pages is: ", len(newList))

pdf = img2pdf.convert(newList)
os.chdir(path0)

file = open("frands.pdf","wb")
file.write(pdf)
file.close()
