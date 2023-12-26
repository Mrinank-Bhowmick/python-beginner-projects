# Import Library
import pandas as pd

import numpy as np

# Import Dataset
# This is a data (dummy) of Financial Market Top 25 News to Train and predict model for overall sentiment analysis.
data = pd.read_csv("Financial Market News.csv", encoding="ISO-8859-1")

# Analysis of dataset
data.head()

data.info()

data.shape

data.columns

# Features selection
" ".join(str(x) for x in data.iloc[1, 2:27])

data.index

len(data.index)

news = []
for row in range(0, len(data.index)):
    news.append(" ".join(str(x) for x in data.iloc[row, 2:27]))

type(news)

news[0]

X = news

type(X)

# creating a bag of words
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(lowercase=True, ngram_range=(1, 1))

X = cv.fit_transform(X)

X.shape

y = data["Label"]

y.shape

# Get train test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=2529
)

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=200)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

confusion_matrix(y_test, y_pred)

print(classification_report(y_test, y_pred))
