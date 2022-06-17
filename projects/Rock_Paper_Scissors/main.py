while True:
    choice, bchoice, value = input("[R]ock, [P]aper, [S]cissors\n: ").lower(), __import__("random").randint(1, 3), 0
    if choice in ["r", "p", "s"]: break
    print("Not r, p, or s\n")

value = ["r", "p", "s"].index(choice)+1

if str(value)+str(bchoice) in ["13", "21", "32"]: print("You win!")
elif str(value) == str(bchoice):                  print("It's a draw!")
else:                                             print("You lose.")
