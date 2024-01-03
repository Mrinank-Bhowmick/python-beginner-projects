import requests

def get_quote_of_the_day():
    api_url = "https://api.quotable.io/random"
    response = requests.get(api_url)

    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data["content"]
        author = quote_data["author"]
        return f'"{quote}" - {author}'
    else:
        return "Failed to fetch a quote. Please try again later."

if __name__ == "__main__":
    quote_of_the_day = get_quote_of_the_day()
    print(quote_of_the_day)
