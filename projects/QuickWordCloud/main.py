import matplotlib.pyplot as plt
from wordcloud import WordCloud


class QuickWordCloud:
    def __init__(self, file_name="./data/test_data.txt"):
        self.file_name = file_name

    def extract_words(self):
        all_words = ""
        with open(self.file_name) as file:
            data = file.read()
        words = data.split()
        words_lower = [w.lower() for w in words]
        all_words += " ".join(words_lower) + " "
        return all_words

    def create_word_cloud(self, text):
        wordcloud = WordCloud(
            width=1600,
            height=800,
            background_color="white",
            collocations=False,
            repeat=True,
        ).generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    wc = QuickWordCloud()
    words = wc.extract_words()
    wc.create_word_cloud(words)
