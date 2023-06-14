import function

print("Hello! Welcome to a Pig Latin converter")
print("=" * 39)
original_string = input(
    "Please type the string you would like to convert to pig latin: "
)

print()
print("Your converted string is:")
print(function.to_pig(original_string))
