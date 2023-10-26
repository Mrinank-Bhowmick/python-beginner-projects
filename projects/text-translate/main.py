# Download the required library
# pip install translate

from translate import Translator


def main():
    while True:
        user_input = input("Enter the text to translate (or 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Exiting the translator.")
            break

        print("Available languages:")
        print("1) English")
        print("2) Spanish")
        print("3) Portuguese")
        print("4) Chinese")
        print("5) French")
        print("6) German")
        print("7) Italian")
        print("8) Japanese")
        print("9) Korean")
        print("10) Russian")
        print("11) Arabic")
        print("12) Dutch")
        print("13) Greek")
        print("14) Hindi")
        print("15) Turkish")
        print("16) Swedish")
        print("17) Polish")
        print("18) Vietnamese")
        print("19) Thai")
        print("20) Hebrew")
        # Add more languages as needed...

        try:
            selected_lang = int(input("Select a target language (1-20): "))
            if selected_lang not in range(1, 21):
                raise ValueError("Invalid option selected.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric option.")
            continue

        languages = {
            1: "en",
            2: "es",
            3: "pt",
            4: "zh",
            5: "fr",
            6: "de",
            7: "it",
            8: "ja",
            9: "ko",
            10: "ru",
            11: "ar",
            12: "nl",
            13: "el",
            14: "hi",
            15: "tr",
            16: "sv",
            17: "pl",
            18: "vi",
            19: "th",
            20: "he",
            # Add more language mappings here...
        }

        target_language = languages[selected_lang]

        try:
            translator = Translator(to_lang=target_language)
            translation = translator.translate(user_input)
            print(f"Translated text ({target_language}): {translation}")
        except Exception as e:
            print(f"Translation failed with error: {str(e)}")


if __name__ == "__main__":
    main()
