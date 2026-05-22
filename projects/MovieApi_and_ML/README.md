# Movie API and ML

A Django web application that exposes a movie API and a machine-learning recommendation system. It combines movie metadata with ML algorithms to provide personalised movie recommendations through a web interface.

## Example

1. Start the Django development server with `python movieapi/manage.py runserver`.
2. Open a browser or API client and navigate to `http://127.0.0.1:8000/`.
3. Browse the available endpoints to query movie metadata and receive ML-based personalised recommendations.
4. The server returns JSON responses with movie details and recommendation results.

## How to run on localhost

```
pip install -r movieapi/requirements.txt
python movieapi/manage.py runserver
```

See `movieapi/README.md` for details on configuring an API key.

## Dependencies

- Django and the packages listed in `movieapi/requirements.txt` (includes scikit-learn, pandas)
