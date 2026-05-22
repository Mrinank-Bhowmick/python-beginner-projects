# Web Scraping Jujustu Kaisen Manga

A simple yet interesting web scraping project to download all the
chapters from Jujustu Kaisen Manga till date.


**Tech Stack :** Python + various modules like `re`, `os`, `bs4 ( beautifulSoup )`, `urllib`, `requests`, `zipfile` and `selenium` ( basic )

<br>

#  Description

Web scraping is an essential tool for gathering data and there are plenty of examples that focus on getting tabular data from websites. I would like to improve on it and extract and download other resources such as images, links, etc. This tutorial covers the following topics in the same order :

- Dealing with **single page applications** and **infinite scrolling websites** using `Selenium`
- Extracting useful links using `BeautifulSoup` and `requests` 
- **Cleaning the data** using custom `Regex`  
- **Downloading all the chapters as jpeg** ( can be customized easily to limit the number of chapters ) :
    - Using `urllib` and `os` module
    - Mocking requests to bypass rate limiting and bot detection 
- Organizing and grouping the chapters
- **Zipping and converting the chapters into `.cbz` format** :
    - Can be extended to Volume based zipping ( For example, Volume 1 has Chapters 1 to 60, Volume 2 has Chapters 61 to 120, and so on )
    - The file format can be customized as well ( For example, .pdf, etc. )



## Example

Running `python app.py` executes three stages and prints progress messages to the console:

```text
1/7 Website loading . . .
2/7 Website loaded . . .
3/7 List elements found . . .
4/7 Iterating through links . . .
5/7 Iterating through links completed . . .
6/7 Writing link to files . . .
7/7 Writing link to files completed . . .
******************* CHAPTER NO ******************* 1
Downloading Images . . .
Downloaded images
...
Zipping chapter_1/chapter_1_0.jpg . . .
Zipping chapter_1/chapter_1_1.jpg . . .
```

Chapter images are saved in per-chapter folders and then zipped into `Jujutsu_Kaisen.cbz`.

# Usage

Install the following packages :

```
pip install beautifulsoup4 selenium
```

**Note that Selenium also requires a webdriver. This project uses
the chrome webdriver** ( download the executable from [here](https://sites.google.com/chromium.org/driver/) and note its absolute path as we will be needing it ) but feel free to use any other web drivers that you see fit.

<br>

> Before running the program, Please read the comment titled IMPORTANT in the `scrape_data()` function in `app.py`. **Directly running the program 
will download ALL the chapters** ( there are currently 192 chapters and each of them has around 30 images ) **which will take about 6 hours.** So, to limit or to choose the exact number of chapters, look into the above mentioned function

<br>

Run the program :

```
python app.py
```

<br>

**Made with 💙 by [Vishvam](https://github.com/Vishvam10)**
