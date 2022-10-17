# SIMPLE AUTOCOMPLETE FEATURE
# Remember to insert a word belonging to the corpus only.
# in some cases it may show index out of range just because it might run out of words after that word.


# **change the text inside training corpus to get sentence completition accordingly**


import re

training_corpus = """This is an example of how an algorithm is able to autocomplete the text you write.
This works good in the case when we use higher level n-gram models to predict the word.
For example, a Trigram model provides more context to an algorithm to work."""

def text_clean_and_tokenize(training_corpus):
	text = training_corpus.lower().split("\n")
	text = [re.sub(u"[^a-zA-Z0-9 -]", "", i) for i in text]
	text = ["<s> " + i + " </s>" for i in text ]
	tokenized_text = " ".join(text).split()
	return tokenized_text

def autocomplete(starting_word, training_corpus):
	tokenized = text_clean_and_tokenize(training_corpus)
	max_freq = 0
	max_probab_word = ""
	freq_dict = {}
	# starting word = <s>
	for i in range(len(tokenized)):
		if tokenized[i] == starting_word:
			if tokenized[i+1] in freq_dict:
				freq_dict[tokenized[i+1]] += 1
			else:
				freq_dict[tokenized[i+1]] = 1

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

