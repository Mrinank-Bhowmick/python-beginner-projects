# NOTE : please import fpdf module before running this program
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)

filename = "reciept.txt"

with open(filename, "w") as f:
    a = f.write("")

f = open(filename, "a")
f.write("*************************  Template Store  *************************\n\n")

sum = 0
i = 1
while True:
    productPurchased = input(
        "Enter the product name (Press q to print the final bill): \n"
    )
    if productPurchased == "q":
        break
    productQuantity = int(input("Enter the product quantity : \n"))
    productCode = input("Enter the product code : \n")
    productPrice = input("Enter the unit price : \n")
    if productPurchased != "q":
        sum = sum + (int(productPrice) * productQuantity)
        billing = f"{i}). \t {productPurchased}  of code  {productCode}  of quantity  \n {productQuantity}  billed  {productPrice}x{productQuantity}units  =  \n \t Rs.{(int(productPrice))*productQuantity}  "
        f.write(billing + "\n")
        print(billing)
        i += 1

print(f"order total so far Rs.{sum}")
thanq = (
    f"\n\n!!! Your bill total is  Rs.{sum} only . Thanks for shopping with us !!!\n\n"
)
f.write(thanq)
print(thanq)

f.close()

# Generate the bill in pdf format
f = open(filename, "r")
for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align="L")
pdf.output("billGenerated.pdf")
f.close()
