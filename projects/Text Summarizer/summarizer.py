import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stop_words = list(STOP_WORDS)
nlp = spacy.load("en_core_web_md")


def summarize(text):
    punctuation = ""
    document = nlp(text)
    len(document)
    tokens = [token.text for token in document]
    print(tokens)

    punctuation = punctuation + "\n"
    print(punctuation)

    wordfreq = {}
    for word in document:
        if word.text.lower() not in stop_words:
            if word.text.lower() not in punctuation:
                if word.text not in wordfreq.keys():
                    wordfreq[word.text] = 1
                else:
                    wordfreq[word.text] += 1
    print(wordfreq)

    word_freq = max(wordfreq.values())
    for word in wordfreq.keys():
        wordfreq[word] = wordfreq[word] / word_freq
    sentence = [sent for sent in document.sents]
    print(sentence)

    sentence_score = {}
    for sent in sentence:
        for word in sent:
            if word.text.lower() in wordfreq.keys():
                if sent not in sentence_score.keys():
                    sentence_score[sent] = wordfreq[word.text.lower()]
                else:
                    sentence_score[sent] += wordfreq[word.text.lower()]

    from heapq import nlargest

    summary_length = int(len(sentence) * 0.3)
    print(sentence_score)

    summary = nlargest(summary_length, sentence_score, key=sentence_score.get)
    final_summary = [word.text for word in summary]
    summary = " ".join(final_summary)

    print(summary)


text = input("Enter the text: ")
summarize(text)
