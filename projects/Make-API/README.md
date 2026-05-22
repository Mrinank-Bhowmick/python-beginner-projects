# Make-API

A small Flask web API that returns a random quote (read from `quote.txt`) as JSON on the root route.

## Example

After starting the server, open `http://127.0.0.1:5000/` in a browser or with curl:

```text
$ curl http://127.0.0.1:5000/
"The only way to do great work is to love what you do."
```

Each request returns a randomly selected quote from `quote.txt` as a JSON string.

## How to run on localhost

```
pip install flask
python app.py
```

Then open http://127.0.0.1:5000/ in a browser.

## Dependencies

flask.
