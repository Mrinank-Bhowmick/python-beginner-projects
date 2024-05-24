from bs4 import BeautifulSoup
import urllib.request as req
import csv


def scrape(file_writer):
    url = "https://www.reuters.com/technology/"
    response = req.urlopen(url)
    data = response.read()
    soup = BeautifulSoup(data, "lxml")
    for article in soup.find_all("article"):
        article_title = article.find("h3", class_="story-title").text.strip()
        print(article_title)

        article_content = article.find("div", class_="story-content").p.text.strip()
        print(article_content)
        article_time = article.find("time", class_="article-time").span.text.strip()
        print(article_time)
        try:
            article_src = article.find("a", href=True)
            article_link = "https://www.reuters.com/{}".format(
                article_src["href"]
            ).strip()
        except Exception as e:
            article_link = None
        print(article_link)
        file_writer.writerow(
            [article_title, article_content, article_time, article_link]
        )


def main():
    csv_file = open("reuters_scrape.csv", "w")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Headline", "Summary", "Time", "Article Link"])
    scrape(csv_writer)
    csv_file.close()


if __name__ == "__main__":
    main()
