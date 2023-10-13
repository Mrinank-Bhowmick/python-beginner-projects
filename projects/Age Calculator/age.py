from datetime import datetime

# Get the current date
current_date = datetime.now()

# Input the birthdate from the user (in yyyy-mm-dd format)
birthdate = input("Enter your birthdate (yyyy-mm-dd): ")

# Convert the birthdate string to a datetime object
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

# Calculate the difference in dates
age = current_date - birthdate

# Calculate years, months, and days
years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30
weeks = age.days // 7

# Display the age
print(f"Your age is: {years} years, {months} months, {days} days, and {weeks} weeks.")
