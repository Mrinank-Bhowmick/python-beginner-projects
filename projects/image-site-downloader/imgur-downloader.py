import os
import requests
import bs4


def downloader(query, max_save, output_path):
    """
    Args:
        query (str): search query
        max_save (int): max number of images to save to results
    Returns:
        None
    """

    # create imgur search url
    searchUrl = "https://imgur.com/search"
    queryUrl = searchUrl + "?q=" + query

    # set up output_path
    abs_output_path = os.path.abspath(output_path)
    os.makedirs(abs_output_path, exist_ok=True)

    # Make request to imgur with query
    res1 = requests.get(queryUrl)

    try:
        res1.raise_for_status()

        # parse res.text with bs4 to images
        imugurSoup = bs4.BeautifulSoup(res1.text, "html.parser")
        images = imugurSoup.select(".image-list-link img")

        # extract number image urls
        num_to_save = min(max_save, len(images))
        download_links = ["https:" + img.get("src") for img in images[:num_to_save]]

        # make requests for extracted url
        for link in download_links:

            # request image link from imgur
            res2 = requests.get(link)

            try:
                res2.raise_for_status()

                # save to file with url base name in folder results
                imgFile = open(
                    os.path.join(abs_output_path, os.path.basename(link)), "wb"
                )
                for chunk in res2.iter_content(100000):
                    imgFile.write(chunk)
                imgFile.close()

            except Exception as exc:
                print("There was a problem: %s" % (exc))

    except Exception as exc:
        print("There was a problem: %s" % (exc))


if __name__ == "__main__":
    downloader("messi", 10, "results")
