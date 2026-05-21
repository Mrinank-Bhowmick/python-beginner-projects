# === Bigram Autocomplete · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @HridayAg0102.

# Import regular expressions library
import re

# Read the training text from the user
training_corpus = input("""Insert the training corpus here (can be multiline)""")


# Clean text and split it into tokens
def text_clean_and_tokenize(training_corpus):
    # Lowercase and split into lines
    text = training_corpus.lower().split("\n")
    # Remove punctuation from each line
    text = [re.sub("[^a-zA-Z0-9 -]", "", i) for i in text]
    # Wrap each line with start/end markers
    text = ["<s> " + i + " </s>" for i in text]
    # Join everything into one flat token list
    tokenized_text = " ".join(text).split()
    return tokenized_text


# Find the most likely word to follow the starting word
def autocomplete(starting_word, training_corpus):
    tokenized = text_clean_and_tokenize(training_corpus)
    max_freq = 0
    freq_dict = {}
    # Count how often each word follows the starting word
    for i in range(len(tokenized)):
        if tokenized[i] == starting_word:
            if tokenized[i + 1] in freq_dict:
                freq_dict[tokenized[i + 1]] += 1
            else:
                freq_dict[tokenized[i + 1]] = 1

    # Pick the word with the highest count
    max_probab_word = ""
    for i in freq_dict:
        if max_freq <= freq_dict[i]:
            max_freq = freq_dict[i]
            max_probab_word = i

    return max_probab_word


if __name__ == "__main__":
    # Start with a single word from the user
    word = [input("insert a word: ")]

    # Predict the next 6 words using bigrams
    for i in range(6):
        word.append(autocomplete(word[i], training_corpus))

    # Print the completed sentence
    print(" ".join(word))
