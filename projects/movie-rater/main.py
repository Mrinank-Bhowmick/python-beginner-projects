from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import requests

load_dotenv()


app = FastAPI(
    title="MOVIE RATER API",
    description="The MovieRater API is your gateway to a world of cinematic exploration and user-generated movie ratings. This versatile API empowers developers to create dynamic movie-related applications, allowing users to rate, review, and discover films from a vast collection.",
    docs_url="/",
)
apiKey = os.getenv("API_KEY")
apiToken = os.getenv("API_TOKEN")


@app.get("/movies")
async def get_popular_movies():
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={apiKey}&sort_by=popularity.desc"

    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.content)

    movie_data = response.json()

    return movie_data


@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int):
    """Get information about a movie."""

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={apiKey}"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.content)

    movie_data = response.json()

    return movie_data


@app.post("/movies/{movie_id}/rate")
async def rate_movie(movie_id: int, rating: int):
    """Rate a movie."""

    # Validate the rating.
    if rating not in range(1, 11):
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 10.")

    # Save the rating to your database.

    # Return a success response.
    return {"message": "Movie rated successfully."}
