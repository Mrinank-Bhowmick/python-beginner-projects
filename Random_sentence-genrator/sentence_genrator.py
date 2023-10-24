import random

# Lists of words for different parts of speech
nouns = ["cat", "dog", "house", "car", "apple"]
verbs = ["runs", "eats", "sleeps", "drives", "jumps"]
adjectives = ["red", "happy", "quick", "tasty", "big"]
adverbs = ["slowly", "quickly", "happily", "loudly", "silently"]

# Function to generate a random sentence
def generate_sentence(num_sentences, use_nouns, use_verbs, use_adjectives, use_adverbs):
    sentence_list = []
    for _ in range(num_sentences):
        sentence = []
        if use_adjectives:
            sentence.append(random.choice(adjectives))
        if use_nouns:
            sentence.append(random.choice(nouns))
        if use_verbs:
            sentence.append(random.choice(verbs))
        if use_adverbs:
            sentence.append(random.choice(adverbs))
        sentence_list.append(" ".join(sentence) + ".")

    return sentence_list

# User input
num_sentences = int(input("Enter the number of sentences to generate: "))
use_nouns = input("Include nouns? (yes/no): ").lower() == "yes"
use_verbs = input("Include verbs? (yes/no): ").lower() == "yes"
use_adjectives = input("Include adjectives? (yes/no): ").lower() == "yes"
use_adverbs = input("Include adverbs? (yes/no): ").lower() == "yes"

sentences = generate_sentence(num_sentences, use_nouns, use_verbs, use_adjectives, use_adverbs)

# Print generated sentences
for sentence in sentences:
    print(sentence)
