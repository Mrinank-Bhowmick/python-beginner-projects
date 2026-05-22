# Movie Recommendation Engine

A content-based movie recommender. It combines movie keywords, cast, genres and director into a single text feature, vectorises it with `CountVectorizer`, computes cosine similarity between all movies, and prints the top 5 movies most similar to a chosen film.

## Example

The script is hard-coded to find movies similar to `"Avatar"` and prints the top 5 results:

```text
Top 5 similar movies to Avatar are:

Guardians of the Galaxy
Aliens
Star Wars: Clone Wars: Volume 1
Star Trek Into Darkness
Alien
```

## How to run on localhost

```
pip install pandas numpy scikit-learn
python movie_recommendation_engine.py
```

`movie_dataset.csv` must be present in the same folder.

## Dependencies

- pandas
- numpy
- scikit-learn
