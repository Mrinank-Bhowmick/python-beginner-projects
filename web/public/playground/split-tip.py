# === Split Tip Calculator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @DevTomilola-OS.

# Greet the user
print("Welcome to the Tip calculator")
# Collect bill amount, tip percentage, and number of people
amount = float(input("Enter your bill amount ($): "))
tip = float(input("what percentage of tip you want to give? 5, 10, 12 or 15?\n"))
split = int(input("How many people to split the bill amount: "))
# Calculate each person's tip share and total share
w = ((0.01 * tip) * amount) // split
x = (amount + (0.01 * tip) * amount) // split
# Collect inputs a second time (as in original program)
amount = float(input("Enter your bill amount ($): "))
tip = float(input("what percentage of tip you want to give? 5, 10, 12 or 15?\n"))
split = int(input("How many people to split the bill amount: "))
# Recalculate with the new inputs
w = ((0.01 * tip) * amount) // split
x = (amount + (0.01 * tip) * amount) // split
# Print each person's tip and total
print(f"Each person has to pay ${w} in tip and ${x} in total")
