import requests
from bs4 import BeautifulSoup

def check_amazon_availability(product_url):
    headers = {
        "User-Agent": "Your User Agent Here"  # You can set a user agent string here
    }

    try:
        response = requests.get(product_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('span', {'id': 'productTitle'}).get_text(strip=True)
        availability = soup.find('span', {'class': 'a-declarative', 'data-asin': True}).get_text(strip=True)

        if "out of stock" in availability.lower():
            print(f"{title} is currently out of stock on Amazon.")
        else:
            print(f"{title} is available on Amazon.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    product_url = "YOUR_PRODUCT_URL_HERE"
    check_amazon_availability(product_url)
