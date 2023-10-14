import tkinter as tk
from textblob import TextBlob

# Define the translation functions
def translate_to_emoji(sentence):
    words = sentence.split()
    translated_sentence = []

    for word in words:
        if word.isalpha():
            emoji = emoji_dict.get(word.lower(), word)
            translated_sentence.append(emoji)
        else:
            translated_sentence.append(word)

    return ' '.join(translated_sentence)

def translate_to_english(sentence):
    reversed_dict = {v: k for k, v in emoji_dict.items()}
    words = sentence.split()
    translated_sentence = []

    for word in words:
        translated_word = reversed_dict.get(word, word)
        translated_sentence.append(translated_word)

    return ' '.join(translated_sentence)

def analyze_sentiment(sentence):
    analysis = TextBlob(sentence)
    sentiment_score = analysis.sentiment.polarity

    if sentiment_score > 0.5:
        return "😃 Very Positive"
    elif sentiment_score > 0:
        return "🙂 Positive"
    elif sentiment_score == 0:
        return "😐 Neutral"
    elif sentiment_score > -0.5:
        return "😕 Negative"
    else:
        return "😠 Very Negative"

# Define the GUI functions
def translate():
    user_input = entry.get()
    sentiment = analyze_sentiment(user_input)
    if translation_mode.get() == 1:  # English to Emoji
        translated_sentence = translate_to_emoji(user_input)
    else:  # Emoji to English
        translated_sentence = translate_to_english(user_input)
    output_label.config(text=f"{sentiment}\n{translated_sentence}")

def set_translation_mode():
    translation_label.config(text="Translate to:" if translation_mode.get() == 1 else "Translate from:")

# Define the emoji dictionary
emoji_dict = {
    # ... (add your emojis and words here)
}

# Create the main window
root = tk.Tk()
root.title("Emoji Translator")

# Create a label and entry for user input
label = tk.Label(root, text="Enter a sentence:")
label.pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create radio buttons for translation mode
translation_mode = tk.IntVar()
english_to_emoji_radio = tk.Radiobutton(root, text="English to Emoji", variable=translation_mode, value=1, command=set_translation_mode)
emoji_to_english_radio = tk.Radiobutton(root, text="Emoji to English", variable=translation_mode, value=2, command=set_translation_mode)
english_to_emoji_radio.pack()
emoji_to_english_radio.pack()

# Create a button to trigger translation
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=10)

# Create a label to display the output
output_label = tk.Label(root, text="", font=("Arial", 14))
output_label.pack(pady=10)

# Create a label to indicate translation direction
translation_label = tk.Label(root, text="Translate to:")
translation_label.pack(pady=5)

# Run the GUI
root.mainloop()
