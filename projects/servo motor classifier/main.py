import pandas as pd

import numpy as np

# Import Data

df = pd.read_csv(
    "https://github.com/YBI-Foundation/Dataset/raw/main/Servo%20Mechanism.csv"
)

# Describe Data

df.head()

df.info()

df.describe()

df.columns

df[["Motor"]].value_counts()

df[["Screw"]].value_counts()

# Data Preprocessing

df.replace({"Motor": {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}}, inplace=True)
df.replace({"Screw": {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}}, inplace=True)

df[["Motor"]].value_counts()

df[["Screw"]].value_counts()

# Define Target Variable (y) and Features Variables (X)

y = df["Class"]

y.shape

y

X = df[["Motor", "Screw", "Pgain", "Vgain"]]

X.shape

X

# Train Test Split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=2529
)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Modeling

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train, y_train)

# Prediction

y_pred = lr.predict(X_test)

y_pred.shape

y_pred

# Model Evaluation

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mean_squared_error(y_test, y_pred)

mean_absolute_error(y_test, y_pred)

r2_score(y_test, y_pred)


# Get Visualization Actual vs Predicted Results

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.show()
