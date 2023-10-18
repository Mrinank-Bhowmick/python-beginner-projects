import img2pdf
import os

list1 = os.listdir(".")
print(list1)
#newList = [x for x in list1 if x.endswith(".png") or x.endswith(".jpg")]
newList = []
for x in list1:
    if x.endswith(".png") or x.endswith(".jpg"):
        newList.append(x)

print("total no of pages is: ", len(newList))

print(newList)
pdf = img2pdf.convert(newList)

file = open("img2pdf.pdf","wb")
file.write(pdf)
file.close()
