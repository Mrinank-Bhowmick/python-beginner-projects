"""
This is a word predictor algorithm, that uses you own Whatsapp chats and shows you prediction.
It takes into account a words and their frequencies after a given word in the texts you have exchanged with a Whatsapp contact.

Requirements:
1 ) You should have pandas installed -- pip install pandas
2 ) You should have whatsapp chats downloaded in you PC as Chats.txt

## To download the whatsapp chats:
1) Open whatsapp on your phone.
2) Pick a contact of your coice, and open their chat
3) Click on the 3 dots on the upper-right side of the chat
4) Go to More -> Export Chat (The chats will the be downloaded)
5) Put it into your PC, and replace the Chats.txt in the Code with the name of the Downloaded txt file (and directly if required)

"""

import pandas as pd


class WhatsAppChat:
    def __init__(self, filename):
        # Initialize the object by reading in the chat file, and counting word frequency and next words
        self.titles = self.read_chat_file(filename)
        self.word_freq_dict = self.count_word_frequency()
        self.next_words_dict = self.find_next_words()

    def read_chat_file(self, filename):
        """Reads in a WhatsApp chat text file and returns a list of titles."""
        chat_df = pd.read_fwf(filename, header=None)
        # Extract the chat titles from the DataFrame and return them as a list
        titles = [title for title in chat_df[2]]
        return titles

    def count_word_frequency(self):
        """Counts the frequency of each word in a list of titles."""
        word_freq_dict = {}
        for title in self.titles:
            # Split each title into words and count their frequency
            for word in str(title).split():
                if len(word) > 1:
                    if word in word_freq_dict.keys():
                        word_freq_dict[word] += 1
                    else:
                        word_freq_dict[word] = 1
        # Sort the word frequency dictionary by value in descending order and return it
        sorted_word_freq_dict = dict(
            sorted(word_freq_dict.items(), key=lambda x: -1 * int(x[1]))
        )
        return sorted_word_freq_dict

    def find_next_words(self):
        """Finds the most common next word for each word in a list of titles."""
        next_words_dict = {}
        for title in self.titles:
            # Split each title into words and count the frequency of each next word for each word
            words = str(title).split()
            for i in range(len(words)):
                if i != len(words) - 1:
                    current_word = words[i]
                    next_word = words[i + 1].replace("\n", "")
                    if current_word in next_words_dict:
                        if next_word in next_words_dict[current_word]:
                            next_words_dict[current_word][next_word] += 1
                        else:
                            next_words_dict[current_word][next_word] = 1
                    else:
                        next_words_dict[current_word] = {next_word: 1}
        # Return the dictionary of next words
        return next_words_dict


class NextWordPredictor:
    def __init__(self, chat, num_predictions=1):
        # Initialize the object with a WhatsAppChat object and the number of predictions to make
        self.chat = chat
        self.num_predictions = num_predictions

    def predict_next_word(self, current_word):
        """Predicts the next word given a current word and a dictionary of next words."""
        if current_word in self.chat.next_words_dict:
            # Get the dictionary of next words for the current word and sort it by frequency
            next_word_freq_dict = self.chat.next_words_dict[current_word]
            sorted_next_words = sorted(
                next_word_freq_dict.items(), key=lambda x: x[1], reverse=True
            )
            # Get the top num_predictions words and return them
            next_words = [word[0] for word in sorted_next_words[: self.num_predictions]]
            return next_words
        else:
            # If the current word is not in the dictionary of next words, return None
            return None


# Create a WhatsAppChat object and a NextWordPredictor object after loading Chats.txt file
# set n as the length of words you want to predict after a given word
chat = WhatsAppChat("Chats.txt")
n, given_word = 3, "good"
predictor = NextWordPredictor(chat, num_predictions=n)

# This prints the next n word predictions after the given_word
print(predictor.predict_next_word(given_word))
