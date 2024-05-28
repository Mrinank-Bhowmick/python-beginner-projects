import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.models.url_shortener import UrlShortenerValidation
from app.services.url_shortener import URLShortener


def run_url_shortener():
    entered_url = input("Enter the URL you want to shorten: ")

    # Validate the entered URL
    url_validation = UrlShortenerValidation(url=entered_url)

    # Extract the validated URL and convert it to string
    validated_url = str(url_validation.url)

    # Pass the string URL to URLShortener
    url_shortener = URLShortener(url=validated_url)

    result = url_shortener.shorten_url()
    if isinstance(result, str):
        print(f"Shortened URL: {result}")
    else:
        print(f"Error occurred: {result}")
    return result


if __name__ == "__main__":
    run_url_shortener()
    # run_url_shortener_with_other_library()

# def run_url_shortener_with_other_library():
#     entered_url = input("Enter the URL you want to shorten: ")

#     # Validate the entered URL
#     url_validation = UrlShortenerValidation(url=entered_url)

#     # Extract the validated URL and convert it to string
#     validated_url = str(url_validation.url)

#     # Pass the string URL to URLShortener
#     url_shortener = URLShortener(url=validated_url, shortener=None) # enter the shortener you want to use

#     result = url_shortener.shorten_url()
#     if isinstance(result, str):
#         print(f"Shortened URL: {result}")
#     else:
#         print(f"Error occurred: {result}")
#     return result
