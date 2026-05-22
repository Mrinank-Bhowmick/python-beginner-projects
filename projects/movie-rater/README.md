# Movie Ratings API

## Overview

This project is a simple Python API that manages movies and their respective ratings. It serves as a centralized hub for movie enthusiasts to share their opinions, discover new films, and assess the quality of movies they've watched.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/) (version 3.3.0 and above)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Virtual Environment](https://docs.python.org/3/library/venv.html) (recommended)

### Installation

1. ## Clone the repository:

   ```bash
     git clone https://github.com/yourusername/your-project.git
     cd your-project
   ```
2. ## Create and activate a virtual environment (optional but recommended):
    ```python -m venv venv
        source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```
3. ## Install the project dependencies:
    ```
    pip install -r requirements.txt

    ```
## Example

Once the server is running, interact with the API at `http://127.0.0.1:8000`:

```text
GET  /movies          → returns a list of popular movies from TMDB
GET  /movies/550      → returns details for the movie with id 550
POST /movies/550/rate?rating=8 → responds with {"message": "Movie rated successfully."}
```

4. ## Running the Application
    ### To run the FastAPI application, use the following command: 

    ```
    uvicorn main:app --reload

    ```
