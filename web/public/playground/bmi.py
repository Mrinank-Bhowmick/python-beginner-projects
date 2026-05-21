# === BMI Calculator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @sudipg4112001.

# Get the user's height and weight
height = float(input("Your height in metres (e.g. 1.75): "))
weight = float(input("Your weight in kilograms (e.g. 70): "))

# Calculate BMI using the standard formula
bmi = weight / (height ** 2)

# Assign a category based on the BMI value
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Display the result and category
print()
print(f"Your BMI is {bmi:.1f}")
print(f"Category: {category}")
