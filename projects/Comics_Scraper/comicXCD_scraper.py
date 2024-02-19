#! python3
import requests, os, bs4, re

url = "https://xkcd.com"
# create a directory to store all the comics
os.makedirs("xkcd", exist_ok=True)


def imgdownloader(url):
    while not url.endswith("#"):
        # print out the current page
        res = requests.get(url)
        res.raise_for_status()  # returns None as the request received is 200 which is fine, if received status is 404 there is an exception for bad request
        soup = bs4.BeautifulSoup(
            res.text, "lxml"
        )  # r.text is the content of the response in unicode, and r.content is the content of the response in bytes.
        # find the comic image on the current page
        comic = soup.select("#comic img")  # finds tag with comic and its sub tag img
        # print(comic)
        if comic == []:
            # the page did not contaib a comic.. move on
            print("No comic was found..")
            break
        else:
            try:
                # get the full url to the comic
                comicimg = "http:" + comic[0].get(
                    "src"
                )  # finds url from the list comic|| basically comic[0] is used as there is just single one element in list!! try print(comic) && print(comic[0]) to see for yourself..
                # check that it is actually a comic and not an interactive page
                if "/comics/" in comicimg:
                    print("Download image %s" % comicimg)
                    res = requests.get(comicimg)
                    res.raise_for_status()
                    # write the image to the xkcd folder
                    image = open(os.path.join("xkcd", os.path.basename(comicimg)), "wb")
                    for chunk in res.iter_content(
                        10000
                    ):  # default way to write requested content basically chunk is byte by byte writing
                        image.write(chunk)
                    image.close()
                    print("Finished")
                    break
                else:
                    print("No comic was found..")
                    break
            except requests.exceptions.MissingSchema:
                print("Error in downloading img!!")
                break


def getLatestComicNumber(url):
    res = requests.get(url)
    res.raise_for_status()  # returns None as the request received is 200 which is fine, if received status is 404 there is an exception for bad request
    soup = bs4.BeautifulSoup(res.text, "lxml")
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prevLink.get("href")
    x = re.findall("\d+", url)
    x = int(x[0]) + 1
    # print(x)
    return x


# this function is basically traversing backwards, it starts from the most recent comic and goes back until n-1 n being number of pages
# as there are no prev before 1 ( :p quite obvious)
def getNextComic(soup):
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prevLink.get(
        "href"
    )  # gets /comic-num/ from current page prev button ..basic crawling!!
    return url


def getSpecificComic(comic_number):  # comic_number
    res = url + "/" + comic_number + "/"
    try:
        imgdownloader(res)
    except Exception as e:
        print(str(e))


def batchDownloader():
    url = "https://xkcd.com"
    # check to make sure it's not the first page
    while not url.endswith("#"):
        # print out the current page
        print("Current page: %s" % url)
        res = requests.get(url)
        res.raise_for_status()  # returns None as the request received is 200 which is fine, if received status is 400
        soup = bs4.BeautifulSoup(
            res.text, "lxml"
        )  # r.text is the content of the response in unicode, and r.content is the content of the response in bytes.
        # find the comic image on the current page
        comic = soup.select("#comic img")  # finds tag with comic and its sub tag img
        # print(comic)
        if comic == []:
            # the page did not contaib a comic.. move on
            print("No comic was found..")
        else:
            try:
                # get the full url to the comic
                comicimg = "http:" + comic[0].get(
                    "src"
                )  # finds url from the list comic|| basically comic[0] is used as there is just single one element in list!! try print(comic) && print(comic[0]) to see for yourself..
                # check that it is actually a comic and not an interactive page
                if "/comics/" in comicimg:
                    print("Download image %s" % comicimg)
                    res = requests.get(comicimg)
                    res.raise_for_status()
                    # write the image to the xkcd folder
                    image = open(os.path.join("xkcd", os.path.basename(comicimg)), "wb")
                    for chunk in res.iter_content(
                        10000
                    ):  # default way to write requested content basically chunk is byte by byte writing
                        image.write(chunk)
                    image.close()
                else:
                    print("No comic was found..")
            except requests.exceptions.MissingSchema:
                url = getNextComic(soup)
                continue
        url = getNextComic(soup)  # basically for downloading the first image
    # all comics have downloaded
    print("Finished")


def main():
    x = int(
        input(
            "Choose your option: \n1.Download all images\t2.Download Specific image\n"
        )
    )
    if x == 1:
        batchDownloader()
    if x == 2:
        y = str(
            input("Enter any comic number between 1-" + str(getLatestComicNumber(url)))
        )
        try:
            getSpecificComic(y)
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    main()
