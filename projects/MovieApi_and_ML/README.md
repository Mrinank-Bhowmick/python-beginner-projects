# Movie API and ML

A Django web application that exposes a movie API and a machine-learning recommendation system. It combines movie metadata with ML algorithms to provide personalised movie recommendations through a web interface.

## How to run

```
pip install -r movieapi/requirements.txt
python movieapi/manage.py runserver
```

See `movieapi/README.md` for details on configuring an API key.

## Dependencies

- Django and the packages listed in `movieapi/requirements.txt` (includes scikit-learn, pandas)

## Pyodide-runnable

No — it is a Django web server project that depends on a server runtime, external APIs and scikit-learn.
