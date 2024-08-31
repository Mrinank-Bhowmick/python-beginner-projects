import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

for random_letter in range(1, nr_letters + 1):
  letter = random.sample(letters, nr_letters)

for random_symbol in range(1, nr_symbols + 1):
  symbol = random.sample(symbols, nr_symbols)

for random_number in range(1, nr_numbers + 1):
  number = random.sample(numbers, nr_numbers)

initial_password = letter + symbol + number
random_password = random.sample(initial_password, len(initial_password))

password_holder = ""

password = password_holder.join(random_password)
print(f"Here is your password: {password}")