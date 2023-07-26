def to_pig(eng_string):
    eng_words = eng_string.split()
    pig_words = []
    vowels = ["a", "e", "i", "o", "u"]
    cap_vowels = ["A", "E", "I", "O", "U"]

    for word in eng_words:
        for i in range(len(word)):
            if word[0] in vowels or word[0] in cap_vowels:
                pig_words.append(word + "yay")
                break

            elif word[0].isupper():
                if word[i] in vowels or word[0] in cap_vowels:
                    remain = word[i:].title()
                    pig_words.append(remain + word[:i].lower() + "ay")
                    break

            else:
                if word[i] in vowels or word[0] in cap_vowels:
                    pig_words.append(word[i:] + word[:i] + "ay")
                    break

    pig_sentence = " ".join(pig_words)
    return pig_sentence
