# Emoji Translator

This is a simple GUI-based Emoji Translator that allows you to convert sentences to emojis and vice versa. The application also provides sentiment analysis of the input sentence.

## Features

- Translate sentences to emojis using a predefined dictionary.
- Translate emojis back to English.
- Analyze the sentiment of the input sentence and display an emoji representing the sentiment.

## How to Use

1. Clone the repository or copy the code into your Python environment.
2. Make sure you have the necessary libraries installed (`tkinter` and `textblob`).
3. Run the Python script.

## Usage

1. Enter a sentence in the provided text box.
2. Choose the translation mode: from English to Emoji or from Emoji to English.
3. Click the "Translate" button.
4. The translated sentence or sentiment analysis will be displayed below.

## Emoji Dictionary

You can customize the emoji dictionary by adding your own words and corresponding emojis.

```python
emoji_dict = {
    'hello': '👋',
    'how': '😊',
    # Add more as needed
}
