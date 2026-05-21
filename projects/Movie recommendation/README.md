# Movie Recommendation Engine

A content-based movie recommender. It combines movie keywords, cast, genres and director into a single text feature, vectorises it with `CountVectorizer`, computes cosine similarity between all movies, and prints the top 5 movies most similar to a chosen film.

## How to run

```
pip install pandas numpy scikit-learn
python movie_recommendation_engine.py
```

`movie_dataset.csv` must be present in the same folder.

## Dependencies

- pandas
- numpy
- scikit-learn

## Pyodide-runnable

No — it depends on `scikit-learn`, which is not available in Pyodide.
