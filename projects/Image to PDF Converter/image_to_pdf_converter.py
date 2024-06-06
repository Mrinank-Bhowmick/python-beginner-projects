"""
This script resizes all the images to A4 size in a given directory and merges them into a single PDF file.
"""

# Import the necessary libraries
from os import listdir
from fpdf import FPDF

# Set the path to the directory containing the images to be converted
path = "convert/"

# Get a list of all the images in the directory
img_list = listdir(path)

# Sort the list of images alphabetically
img_list.sort()

# Create a new FPDF object
pdf = FPDF("P", "mm", "A4")

# Set the initial coordinates for the image
x = 0
y = 0

# Set the width and height of the image
w = 210
h = 297

# Iterate over the list of images
for img in img_list:

    # Add a new page to the PDF
    pdf.add_page()

    # Add the image to the PDF
    pdf.image(path + img, x, y, w, h)

# Output the PDF file
pdf.output("output.pdf", "F")
