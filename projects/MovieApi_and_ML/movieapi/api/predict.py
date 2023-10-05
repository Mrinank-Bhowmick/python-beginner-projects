import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df1 = pd.read_csv(r"tmdb-movie-metadata\tmdb_5000_movies.csv")


count = CountVectorizer(stop_words="english")
df1["overview"] = df1["overview"].fillna("")
count_matrix = count.fit_transform(df1["overview"])


cosine_similarity_count = cosine_similarity(count_matrix, count_matrix)

indices = pd.Series(df1.index, index=df1["title"]).drop_duplicates()


# Using TFIDF
def get_recommendations(title, cosine_sim=cosine_similarity_count):
    try:
        # Get the index of the movie that matches the title
        idx = indices[title]

        # Get the pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:2]  # Adjust this number as needed

        # Get the titles of the recommended movies
        recommended_movies = recommended_movies = df1["title"].iloc[sim_scores[0][0]]

        return recommended_movies
    except KeyError:
        return "Sorry, we don't have enough data about this movie title."
