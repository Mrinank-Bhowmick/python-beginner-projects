import requests

def get_quote_of_the_day():
    # Fetch a random quote from the Quotable API
    api_url = "https://api.quotable.io/random"
    response = requests.get(api_url)

    if response.status_code == 200:
        # Extract quote content and author from the API response
        quote_data = response.json()
        quote = quote_data["content"]
        author = quote_data["author"]
        return f'"{quote}" - {author}'
    else:
        # Return a message in case of a failed API request
        return "Failed to fetch a quote. Please try again later."

def print_quote_of_the_day():
    # Print the quote of the day to the console
    quote_of_the_day = get_quote_of_the_day()
    print(quote_of_the_day)

if __name__ == "__main__":
    # Invoke the function to print the quote of the day when the script is run
    print_quote_of_the_day()
