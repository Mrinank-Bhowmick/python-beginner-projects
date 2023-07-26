# Import the FPDF library for creating PDF documents
from fpdf import FPDF

# Create an instance of the FPDF class
pdf = FPDF()

# Add a page to the PDF document
pdf.add_page()

# Set the font for the text in the PDF
pdf.set_font("Arial", size=15)

# Define the filename for the receipt text file
filename = "receipt.txt"

# Create or clear the content of the receipt text file
with open(filename, "w") as f:
    a = f.write("")

# Open the receipt text file in append mode
f = open(filename, "a")

# Write the store name and header to the receipt text file
f.write("*************************  Template Store  *************************\n\n")

# Initialize variables for calculating the total bill
sum = 0
i = 1

# Begin a loop to collect product information and calculate the bill
while True:
    # Prompt the user to enter the product name or 'q' to print the final bill
    productPurchased = input(
        "Enter the product name (Press q to print the final bill): \n"
    )

    # If the user enters 'q', break the loop and proceed to printing the bill
    if productPurchased == "q":
        break

    # Prompt the user to enter the product quantity
    productQuantity = int(input("Enter the product quantity : \n"))

    # Prompt the user to enter the product code
    productCode = input("Enter the product code : \n")

    # Prompt the user to enter the unit price of the product
    productPrice = input("Enter the unit price : \n")

    # If the user did not enter 'q', calculate the total cost of the product and add it to the overall sum
    if productPurchased != "q":
        sum = sum + (float(productPrice) * productQuantity)

        # Create a string to represent the billing information for the current product
        billing = f"{i}). \t {productPurchased} of code {productCode}, quantity of {productQuantity} \n billed  {productPrice}x{productQuantity} units  =  \n \t Rs. {(float(productPrice))*productQuantity}  "

        # Write the billing information to the receipt text file
        f.write(billing + "\n")

        # Print the billing information to the console
        print(billing)

        # Increment the counter for the next product
        i += 1

# Print the total order amount calculated so far
print(f"order total so far Rs. {sum}")

# Create a string to thank the customer for shopping and display the total bill amount
thanq = (
    f"\n\n!!! Your bill total is only Rs. {sum}. Thanks for shopping with us !!!\n\n"
)

# Write the thank-you message to the receipt text file
f.write(thanq)

# Print the thank-you message to the console
print(thanq)

# Close the receipt text file after writing all the information
f.close()

# Generate the bill in PDF format

# Open the receipt text file in read mode
f = open(filename, "r")

# Iterate through each line of the receipt text file
for x in f:
    # Add each line of text from the receipt to the PDF document, aligned to the left
    pdf.cell(200, 10, txt=x, ln=1, align="L")

# Save the generated PDF file with the name "billGenerated.pdf"
pdf.output("billGenerated.pdf")

# Close the receipt text file
f.close()
