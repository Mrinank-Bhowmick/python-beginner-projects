# Word Predictor

A next-word prediction tool that learns from an exported WhatsApp chat. It reads a `Chats.txt` file, builds word-frequency and next-word tables, and predicts the most likely words to follow a given word.

## How to run

```bash
pip install pandas
python main.py
```

Place an exported WhatsApp chat as `Chats.txt` in the same folder.

## Dependencies

- pandas

## Pyodide-runnable

No — although `pandas` is available in Pyodide, the script reads a local `Chats.txt` file from the real filesystem, which is not present in the browser sandbox.
