# Download the required library
# pip install translate

from translate import Translator

# to get the input
user_input = input("Enter the text: ")

#  Available languages https://en.wikipedia.org/wiki/ISO_639-1
languages = {1: "en", 2: "es", 3: "pt", 4: "zh"}

while True:
    selected_lang = int(
        input("Translate in 1) English  2) Spanish 3) Portuguese 4) Chinese : ")
    )
    if selected_lang in languages:
        translator = Translator(to_lang=languages[selected_lang])
        break
    else:
        print("Please select a valid option!")
        continue


translation = translator.translate(user_input)

print(translation)
