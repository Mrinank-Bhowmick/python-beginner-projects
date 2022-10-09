print("Welcome to the Tip calculator")
amount = float(input("Enter your bill amount ($): "))
tip = float(input("what percentage of tip you want to give? 5, 10, 12 or 15?\n"))
split = int(input("How many people to split the bill amount: "))
w = ((0.01 * tip) * amount) // split
x = (amount + (0.01 * tip) * amount) // split
amount = float(input("Enter your bill amount ($): "))
tip = float(input("what percentage of tip you want to give? 5, 10, 12 or 15?\n"))
split = int(input("How many people to split the bill amount: "))
w = ((0.01 * tip) * amount) // split
x = (amount + (0.01 * tip) * amount) // split
print(f"Each person has to pay ${w} in tip and ${x} in total")
