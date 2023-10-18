//Merge multiple image files to pdf
import img2pdf
import os

list1 = os.listdir(".")
print(list1)
#newList = [x for x in list1 if x.endswith(".png") or x.endswith(".jpg")]
//Get image file names and extensions
newList = []
for x in list1:
    if x.endswith(".png") or x.endswith(".jpg"):
        newList.append(x)
//Get number of files
print("total no of pages is: ", len(newList))

print(newList)
pdf = img2pdf.convert(newList)   //Get data from list of image files

file = open("img2pdf.pdf","wb")  //Open or create pdf file
file.write(pdf)                  //Write image data to pdf
file.close()                     //Close the file
