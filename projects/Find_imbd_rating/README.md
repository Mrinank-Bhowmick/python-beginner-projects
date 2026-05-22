# Find IMDb Rating

Reads the names of film files from a local directory, searches IMDb for each title, scrapes the rating and genre, and writes the results to `film_ratings.csv`.

## Example

```text
Enter the path where your films are: /home/user/films
https://www.imdb.com/search/title/?title=inception
https://www.imdb.com/search/title/?title=the+dark+knight
https://www.imdb.com/search/title/?title=interstellar
```

After the script finishes, `film_ratings.csv` is written with columns `Film Name`, `Rating`, and `Genre`:

```text
Film Name,Rating,Genre
Inception,8.8," Sci-Fi, Thriller"
The Dark Knight,9.0," Action, Crime, Drama"
Interstellar,8.6," Adventure, Drama, Sci-Fi"
```

## How to run on localhost

```
pip install beautifulsoup4 requests pandas
python Find_imbd_rating.py
```

## Dependencies

- beautifulsoup4
- requests
- pandas
