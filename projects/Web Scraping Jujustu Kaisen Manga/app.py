import os
import re
import requests
from zipfile import ZipFile
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def get_all_chapter_links():

    # Importing Selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Absolute path to the web driver. Here, we are using
    # the chrome web driver but any of the available ones
    # would do as well. Make sure to download the webdriver
    # executable from :
    # https://sites.google.com/chromium.org/driver/
    # before running this code
    path = "C:\Program Files (x86)\chromedriver.exe"

    # This is the website that we will be using.
    # There might be redirections as the site changes
    # its URL frequently, but for the time being
    # this does not cause any errors.
    url = "https://jujmanga.com"

    # Sample chapter URL :
    # https://jujutsu.jujmanga.com/manga/jujutsu-kaisen-chapter-189/

    # Notice that the link for each chapter has the word "manga"
    # This is important because there are multiple links ( for eg.
    # advertisement links, etc. ) in the page that is
    # captured by the variable "links".
    pattern = r"\b\/manga\/\b"

    print("1/7 Website loading . . .")
    driver = webdriver.Chrome(path)

    print("2/7 Website loaded . . .")
    driver.get(url)

    # Finding all the HTML anchor tags
    links = driver.find_elements(by=By.TAG_NAME, value="a")
    print("3/7 List elements found . . .")

    x = []

    print("4/7 Iterating through links . . .")
    for l in links:
        link = l.get_attribute("href")
        if type(link) == str:
            # Getting only chapter links
            if re.search(pattern, link):
                x.append(link)
    print("5/7 Iterating through links completed . . .")

    # Finished extracting all the required links
    # so, quiting the selenium driver
    driver.quit()

    # Writing the links to a file. We could just store
    # it in a list but this kind of persists the data.
    # So, if in the future, you want to use this or check
    # the URL pattern, you could do so without using
    # selenium web driver.
    content = "\n".join(x)
    print("6/7 Writing link to files . . .")

    with open("links.txt", "w") as f:
        f.write(content)
    f.close()

    print("7/7 Writing link to files completed . . .")


def scrape_data():

    f = open("links.txt", "r")
    chapters = f.readlines()
    f.close()

    # Sample chapter link
    # https://jujutsu.jujmanga.com/manga/jujutsu-kaisen-chapter-189/

    # Cleaning all the chapter  links and sorting them
    # numerically ( note that initially they were strings )
    chapters = sorted(
        chapters, key=lambda x: int(x.split("-")[3].replace("\n", "").replace("/", ""))
    )

    # Iterating through every chapter link

    # ************ IMPORTANT ****************
    # Change the range to get the exact number of chapters.
    # Take a look at the links.txt file that is generated to
    # get a sense of indexing because the LATEST CHAPTER
    # WILL BE THE FIRST INDEX of "chapters" array. So, keep
    # that in mind.
    #
    # Also, running this WOULD TAKE A LOT OF TIME ( it took me about 6
    # hours ) as there are currently 192 chapters and each chapter
    # has about 30 images.
    #
    # My suggestion would be to specify the exact number of chapters
    # you want instead of downloading everything.

    # ************ CHANGE THE RANGE ************
    for i in range(len(chapters)):
        chapter = chapters[i]

        chapter = (
            chapter.split("jujutsu-kaisen-")[1]
            .replace("/", "")
            .replace("\n", "")
            .replace("manga", "chapter")
            .replace("-", "_")
        )

        chapter_no = int(chapter.split("_")[1])

        print("******************* CHAPTER NO *******************", chapter_no)
        file_paths = []

        # Get the HTML content of that chapter
        r = requests.get(chapters[i])

        # Parse the HTML
        soup = BeautifulSoup(r.content, features="html.parser")

        # Get all the images
        images = soup.find_all("img")

        # Creating a separate folder for each chapter
        folder_name = "{}".format(chapter)
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r"{}".format(folder_name))
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        print("\nDownloading Images . . .")
        for i in range(len(images)):
            image = images[i]

            # All the static contents are hosted elsewhere. So, we need
            # to find the host. This can be achieved by inspecting the
            # "src" attribute in the image tag
            src = image["src"]

            # Check to see whether the image comes from a trusted domain
            # Not necessary but there might images that are hosted by
            # the website itself and we don't want those images.
            # Please take a look at the dev tools to get a better idea
            # behind this.
            if re.match(r"^https?://", src):

                # Dynamically creating the file name for every image
                # in a given chapter. Please feel free to change
                # this to your liking
                fname = "{}/{}_{}.jpg".format(chapter, chapter, i)
                file_paths.append(fname)

                # Downloading the file :
                # 1. Open a new file
                # 2. Read the incoming request (here, it is an image)
                #    in a raw binary form
                # 3. Save it the file and close the file

                f = open(fname, "wb")

                # The headers were necessary because the website blocked
                # automated requests. So, to bypass it, we mimic human
                # behaviour by adding a header stating that the request
                # was indeed genuine and was made from the mentioned
                # agent. We could be other agents as well
                req = Request(url=src, headers={"User-Agent": "Mozilla/5.0"})
                try:
                    f.write(urlopen(req).read())
                finally:
                    f.close()

        print("\nDownloaded images")


def zip_files():
    file_paths = []
    for (root, dirs, files) in os.walk("./"):
        for f in files:
            fname = "{}/{}".format(root, f)
            file_paths.append(fname)

    # Sort numerically wrt Chapter No. then the Image No.
    file_paths = sorted(
        file_paths[4:],
        key=lambda x: (
            int(re.sub("\D", "", x.split("_")[1])),
            int(re.sub("\D", "", x.split("_")[-1])),
        ),
    )

    # Zipping ALL the chapters into 1 .cbz
    # NOTE : The file size can be huge ( around 1 GB ) if
    # you plan to download all the chapters
    with ZipFile("Jujutsu_Kaisen.cbz", "w") as zip:
        for file in file_paths:
            msg = "Zipping {} . . . ".format(file)
            print(msg)
            zip.write(file)


if __name__ == "__main__":
    get_all_chapter_links()
    scrape_data()
    zip_files()
