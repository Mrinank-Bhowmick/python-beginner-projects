import requests
import bs4


def verify(url):
    """verifies all links within a page, prints broken links
    Args:
        url (str): url of page to check
    Returns:
        None
    """

    res1 = requests.get(url)

    try:
        res1.raise_for_status()

        soup = bs4.BeautifulSoup(res1.text, "html.parser")
        pageLinks = [link.get("href") for link in soup.select("a") if link.get("href")]

        brokenCount = 0
        goodCount = 0

        for link in pageLinks:

            if link.startswith("http"):
                res2 = requests.get(link)

                try:

                    res2.raise_for_status()
                    print(f"Good: {link}")
                    goodCount += 1

                except Exception as exc:
                    print(f"Broken: {link}")
                    brokenCount += 1

        print(f"{goodCount} Good. {brokenCount} Broken")

    except Exception as exc:
        print("There was a problem: %s" % (exc))


if __name__ == "__main__":
    verify("https://automatetheboringstuff.com/chapter11/")
