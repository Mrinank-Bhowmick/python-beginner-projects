# BMI Calculator
# Asks for your height and weight, then tells you your Body Mass Index.

height = float(input("Your height in metres (e.g. 1.75): "))
weight = float(input("Your weight in kilograms (e.g. 70): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print()
print(f"Your BMI is {bmi:.1f}")
print(f"Category: {category}")
