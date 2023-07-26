import requests
from bs4 import BeautifulSoup
import lxml
import csv


def get_article_and_link(url_link, filename):
    request = requests.get(url_link)

    soup = BeautifulSoup(request.text, "lxml")

    article_title_list = ["ARTICLE TITLE"]
    article_link_list = ["ARTICLE LINKS"]

    for article in soup.select(".titleline"):
        article_title_list.append(article.text)
        article_link_list.append(article.select_one("a").get("href"))

    with open(filename, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        for article in zip(article_title_list, article_link_list):
            writer.writerow(article)

    print("Done")


get_article_and_link("https://news.ycombinator.com/news", "ycombinatornews.csv")
