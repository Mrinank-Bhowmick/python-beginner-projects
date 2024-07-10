# Download the required library
# pip install translate

from translate import Translator
from requests.exceptions import RequestException

LANGUAGES = {
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


def get_user_input():
    return input("Enter the text to translate (or 'exit' to quit): ")


def display_languages():
    print("Available languages:")
    for index, language in LANGUAGES.items():
        print(f"{index}) {language.capitalize()}")


def get_target_language():
    while True:
        try:
            selected_lang = int(input("Select a target language (1-20): "))
            if selected_lang not in LANGUAGES:
                raise ValueError("Invalid option selected.")
            return LANGUAGES[selected_lang]
        except ValueError:
            print("Invalid input. Please enter a valid numeric option.")


def translate_text(user_input, target_language):
    try:
        translator = Translator(to_lang=target_language)
        translation = translator.translate(user_input)
        print(f"Translated text ({target_language}): {translation}")
    except RequestException as e:
        print(f"Translation failed. Request error: {str(e)}")
    except Exception as e:
        print(f"Translation failed with error: {str(e)}")


def main():
    while True:
        user_input = get_user_input()

        if user_input.lower() == "exit":
            print("Exiting the translator.")
            break

        display_languages()
        target_language = get_target_language()

        translate_text(user_input, target_language)


if __name__ == "__main__":
    main()
