# Word Predictor

A next-word prediction tool that learns from an exported WhatsApp chat. It reads a `Chats.txt` file, builds word-frequency and next-word tables, and predicts the most likely words to follow a given word.

## Example

With `Chats.txt` in place, running `python main.py` loads the chat, builds word-frequency tables, and prints the 3 most likely words to follow `"good"`:

```text
['morning', 'night', 'luck']
```

The predictions reflect the actual words that most frequently appear after `"good"` in the exported chat file.

## How to run on localhost

```bash
pip install pandas
python main.py
```

Place an exported WhatsApp chat as `Chats.txt` in the same folder.

## Dependencies

- pandas
