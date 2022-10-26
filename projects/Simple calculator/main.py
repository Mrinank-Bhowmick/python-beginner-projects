from functions import *
from constants import *

# Data input
firstValue = int(input("Insert first value : "))
secondValue = int(input("Inser second value: "))
operation = input("Functions: + .. - .. * .. /\n" "Choose your operation: ")

# Rules
if operation == SUM:
    print(sum(firstValue, secondValue))

elif operation == SUBTRATION:
    print(subtraction(firstValue, secondValue))

elif operation == MULTPLICATION:
    print(multiplication(firstValue, secondValue))

else:
    print(division(firstValue, secondValue))
