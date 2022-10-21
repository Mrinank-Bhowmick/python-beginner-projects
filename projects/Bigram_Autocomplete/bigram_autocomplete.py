# SIMPLE AUTOCOMPLETE FEATURE
# Remember to insert a word belonging to the corpus only.
# in some cases it may show index out of range just because it might run out of words after that word.


# **change the text inside training corpus to get sentence completition accordingly**


import re

training_corpus = input("""Insert the training corpus here (can be multiline)""")


# Function for cleaning and tokenizing the text.
# 1st line converts complete text string to lower case and splits it.
# 2nd line uses regex to remove all punctuation marks and special characters ...
# to space from all splitted text statements.

# 3rd line pads the statements with <s> and </s> as starting and ending of statements.
# 2nd last line rejoins the clean and padded text and it is finally returned.


def text_clean_and_tokenize(training_corpus):
    text = training_corpus.lower().split("\n")
    text = [re.sub("[^a-zA-Z0-9 -]", "", i) for i in text]
    text = ["<s> " + i + " </s>" for i in text]
    tokenized_text = " ".join(text).split()
    return tokenized_text


# This function just calculates the frequencies of various ...
# pairs of words which occur together.
# The most frequent pair of words forms the highest probability ...
# of the 2nd word following the first.


def autocomplete(starting_word, training_corpus):
    tokenized = text_clean_and_tokenize(training_corpus)
    max_freq = 0
    freq_dict = {}
    # starting word = <s>
    for i in range(len(tokenized)):
        if tokenized[i] == starting_word:
            if tokenized[i + 1] in freq_dict:
                freq_dict[tokenized[i + 1]] += 1
            else:
                freq_dict[tokenized[i + 1]] = 1

    max_probab_word = ""
    for i in freq_dict:
        if max_freq <= freq_dict[i]:
            max_freq = freq_dict[i]
            max_probab_word = i

    return max_probab_word


if __name__ == "__main__":
    word = [input("insert a word: ")]

    for i in range(6):
        word.append(autocomplete(word[i], training_corpus))

    print(" ".join(word))


#####################################

# CODE CONTRIBUTED BY: HRIDAY AGRAWAL
# GITHUB ID: HridayAg0102

#####################################
