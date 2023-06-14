from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# Initialize a session for consistent parameters across requests
s = requests.session()

# Initialize lists to store data
films = []
names = []
ratings = []
genres = []

# Request user input for the directory containing film files
# For eg: "C:/Users/utkarsh/Desktop/films"
path = input("Enter the path where your films are: ")

# Retrieve and store names of all files in the directory
filmswe = os.listdir(path)

# Remove file extensions from each film name and store in 'films' list
for film in filmswe:
    films.append(os.path.splitext(film)[0])
    # print(os.path.splitext(film)[0])

# Now for every film in our 'films' list
for line in films:
    # x = line.split(", ")
    # Convert the title to lowercase (standardizing for search)
    title = line.lower()
    # release = x[1]
    # Replace spaces with "+" to format for IMDB search query
    query = "+".join(title.split())

    # Create URL for IMDB search
    URL = "https://www.imdb.com/search/title/?title=" + query
    print(URL)
    # print(release)

    # Initiate a try-except block to handle potential exceptions while sending requests or parsing data
    try:
        # Send a GET request to the IMDB page using the session
        response = s.get(URL)

        # Get the content of the page from the response
        content = response.content
        # print(response.status_code)

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, features="html.parser")

        # Find and store all containers with class 'lister-item-content' (holds film data)
        containers = soup.find_all("div", class_="lister-item-content")

        # Loop through each container to extract data
        for result in containers:
            # Extract the film's name (both original and lowercase for our search)
            name1 = result.h3.a.text
            name = result.h3.a.text.lower()

            # Uncomment below lines if you want year specific as well, define year variable before this
            # year = result.h3.find(
            # "span", class_="lister-item-year text-muted unbold"
            # ).text.lower()

            # If the title of the film from our list is found in the scraped names
            if title in name:
                # Extract film rating and genre from container and append to respective lists
                rating = result.find("div", class_="inline-block ratings-imdb-rating")[
                    "data-value"
                ]
                genre = result.p.find("span", class_="genre")
                genre = genre.contents[0]

                # Append the original name, rating and genre to the respective lists
                names.append(name1)
                ratings.append(rating)
                genres.append(genre)

    # In case of an error during the request or data extraction process, print an error message
    except Exception:
        print("Try again with valid combination of title and release year")

# Construct a DataFrame from the extracted data and save as a CSV file
df = pd.DataFrame({"Film Name": names, "Rating": ratings, "Genre": genres})
df.to_csv("film_ratings.csv", index=False, encoding="utf-8")
