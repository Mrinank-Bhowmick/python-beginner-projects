import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
sw = list(STOP_WORDS)
nlp = spacy.load('en_core_web_md')


def sum1(text):
    punctuation = ''
    doc = nlp(text)
    len(doc)
    tokens = [token.text for token in doc]
    print(tokens)

    punctuation = punctuation+'\n'
    print(punctuation)

    wordfreq = {}
    for word in doc:
        if word.text.lower() not in sw:
            if word.text.lower() not in punctuation:
                if word.text not in wordfreq.keys():
                    wordfreq[word.text] = 1
                else:
                    wordfreq[word.text] += 1
    print(wordfreq)

    s = max(wordfreq.values())
    for word in wordfreq.keys():
        wordfreq[word] = wordfreq[word]/s
    st = [sent for sent in doc.sents]
    print(st)

    ss = {}
    for sent in st:
        for word in sent:
            if word.text.lower() in wordfreq.keys():
                if sent not in ss.keys():
                    ss[sent] = wordfreq[word.text.lower()]
                else:
                    ss[sent] += wordfreq[word.text.lower()]

    from heapq import nlargest
    sl = int(len(st)*0.3)
    print(ss)

    summary = nlargest(sl, ss, key=ss.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    print(summary)


text = input('Enter the text: ')
sum1(text)
