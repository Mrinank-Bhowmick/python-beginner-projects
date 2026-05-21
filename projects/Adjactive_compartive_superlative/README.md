# Adjective Comparative & Superlative

A console tool that takes a comma-separated list of adjectives and prints the
comparative and superlative form of each, using WordNet (via NLTK) with a
JSON fallback list of irregular adjectives.

## How to run

```bash
pip install -r requirements.txt
python adjCS.py
```

On first run NLTK downloads the `wordnet` corpus.

## Dependencies

- `nltk` — and its `wordnet` corpus (downloaded at runtime)

## Pyodide-runnable

No. `nltk.download()` fetches the WordNet corpus over the network at runtime,
which is not available in the in-browser Pyodide playground.
