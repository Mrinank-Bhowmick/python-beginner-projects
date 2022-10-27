import requests
from bs4 import BeautifulSoup

url = "https://free-proxy-list.net/"

data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

table = soup.find("table", class_="table")

for row in table.tbody.find_all("tr"):
    columns = row.find_all("td")

    if columns != []:
        ip = columns[0].text.strip()
        port = columns[1].text.strip()
        with open("proxies.txt", "a") as f:
            f.write(f"{ip}:{port}\n")
