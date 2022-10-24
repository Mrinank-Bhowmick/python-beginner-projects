#by vansh
from barcode import EAN13
  

number = '672511672323'
  

my_code = EAN13(number)
  

my_code.save("new_code")