print("Enter the values of sides of a triangle")
a = float(input("Enter the value of side a: "))
b = float(input("Enter the value of side b: "))
c = float(input("Enter the value of side c: "))

# Calculating the values of sin, cos and tan
sin_a = round((a / c), 2)
cos_a = round((b / c), 2)
tan_a = round((a / b), 2)

# Calculating the values of cosec, sec and cot
cosec_a = round((1 / sin_a), 2)
sec_a = round((1 / cos_a), 2)
cot_a = round((1 / tan_a), 2)

# Printing the values of sin, cos and tan
print("\nThe value of sin a is: ", sin_a)
print("The value of cos a is: ", cos_a)
print("The value of tan a is: ", tan_a)

# Printing the values of cosec, sec and cot
print("The value of cosec a is: ", cosec_a)
print("The value of sec a is: ", sec_a)
print("The value of cot a is: ", cot_a)


# Defining the formula of Heron's to calculate the area of triangle.
def Area(a, b, c):
    sp = (a + b + c) / 2
    area = (sp) * (sp - a) * (sp - b) * (sp - c)
    f_area = round((area**0.5), 2)
    print(f"The area of triangle is {f_area}" + " square units")


# Printing the area of triangle.
Area(a, b, c)
