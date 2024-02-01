import pandas as pd
import numpy as np

# importing data
df = pd.read_csv("WhiteWineQuality.csv")

# data inspection
df.head()
df.info()
df.describe()
df.columns
df.shape

# Assigning target variables X and y
df["quality"].value_counts()

df.groupby("quality").mean()

y = df["quality"]

y.shape

y

X = df[
    [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "free sulphur dioxide",
        "total sulphur dioxide",
        "density",
        "pH",
        "sulphates",
        "alchol",
    ]
]

X = df.drop(["quality"], axis=1)

X.shape

X

# Preprocessing the data
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

X = ss.fit_transform()

X

# Spliting the data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=2529)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Training model
from sklearn.svm import SVC

svc = SVC()

svc.fit(X_train, y_train)

y_pred = svc.pred(X_test)

y_pred.shape

y_pred

# Evaluating model
from sklearn.metrics import confusion_matrix, classification_report

print(confusion_metrix(y_test, y_pred))

print(classification_report(y_test, y_pred))
