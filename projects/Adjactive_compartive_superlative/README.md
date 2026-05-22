# Adjective Comparative & Superlative

A console tool that takes a comma-separated list of adjectives and prints the
comparative and superlative form of each, using WordNet (via NLTK) with a
JSON fallback list of irregular adjectives.

## Example

```text
Enter a list of adjectives (comma-separated): happy, bad, large

Adjective       Comparative     Superlative
------------------------------------------
happy           happier         happiest
bad             worse           worst
large           more large      most large
```

## How to run on localhost

```bash
pip install -r requirements.txt
python adjCS.py
```

On first run NLTK downloads the `wordnet` corpus.

## Dependencies

- `nltk` — and its `wordnet` corpus (downloaded at runtime)
