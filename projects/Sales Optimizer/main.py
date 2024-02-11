# Import Libraries
import pandas as pd

import numpy as np

# Import Data

df = pd.read_csv("sales_data.csv")

# Describe Data

df.head()

df.info()

df.columns

df.describe()

# Data Visualization

import seaborn as sns

sns.pairplot(df)

# Data Preprocessing

df["Item_Weight"].fillna(
    df.groupby(["Item_Type"])["Item_Weight"].transform("mean"), inplace=True
)

df.info()

df.describe()

df[["Item_Identifier"]].value_counts()

df[["Item_Fat_Content"]].value_counts()

df.replace(
    {"Item_Fat_Content": {"LF": "Low Fat", "reg": "Regular", "low fat": "Low Fat"}},
    inplace=True,
)

df[["Item_Fat_Content"]].value_counts()

df.replace({"Item_Fat_Content": {"Low Fat": 0, "Regular": 1}}, inplace=True)

df[["Item_Type"]].value_counts()

df.replace(
    {
        "Item_Type": {
            "Fruits and Vegetables": 0,
            "Snack Foods": 0,
            "Household": 1,
            "Frozen Foods": 0,
            "Dairy": 0,
            "Baking Goods": 0,
            "Canned": 0,
            "Health and Hygiene": 1,
            "Meat": 0,
            "Soft Drinks": 0,
            "Breads": 0,
            "Hard Drinks": 0,
            "Others": 2,
            "Starchy Foods": 0,
            "Breakfast": 0,
            "Seafood": 0,
        }
    },
    inplace=True,
)

df[["Item_Type"]].value_counts()

df[["Outlet_Identifier"]].value_counts()

df.replace(
    {
        "Outlet_Identifier": {
            "OUT027": 0,
            "OUT013": 1,
            "OUT035": 2,
            "OUT046": 3,
            "OUT049": 4,
            "OUT045": 5,
            "OUT018": 6,
            "OUT017": 7,
            "OUT010": 8,
            "OUT019": 9,
        }
    },
    inplace=True,
)

df[["Outlet_Identifier"]].value_counts()

df[["Outlet_Size"]].value_counts()

df.replace({"Outlet_Size": {"Small": 0, "Medium": 1, "High": 2}}, inplace=True)

df[["Outlet_Size"]].value_counts()

df[["Outlet_Location_Type"]].value_counts()

df.replace(
    {"Outlet_Location_Type": {"Tier 1": 0, "Tier 2": 1, "Tier 3": 2}}, inplace=True
)

df[["Outlet_Location_Type"]].value_counts()

df[["Outlet_Type"]].value_counts()

df.replace(
    {
        "Outlet_Type": {
            "Grocery Store": 0,
            "Supermarket Type1": 1,
            "Supermarket Type2": 2,
            "Supermarket Type3": 3,
        }
    },
    inplace=True,
)

df[["Outlet_Type"]].value_counts()

df.head()

df.info()

df.shape

df.columns

# Define Target variable(y) and Features Variables(X)

y = df["Item_Outlet_Sales"]

y.shape

y

X = df[
    [
        "Item_Weight",
        "Item_Fat_Content",
        "Item_Visibility",
        "Item_Type",
        "Item_MRP",
        "Outlet_Identifier",
        "Outlet_Establishment_Year",
        "Outlet_Size",
        "Outlet_Location_Type",
        "Outlet_Type",
    ]
]

X.shape

X

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_std = df[["Item_Weight", "Item_Visibility", "Item_MRP", "Outlet_Establishment_Year"]]

X_std = sc.fit_transform(X_std)

X_std

X[["Item_Weight", "Item_Visibility", "Item_MRP", "Outlet_Establishment_Year"]] = (
    pd.DataFrame(
        X_std,
        columns=[
            ["Item_Weight", "Item_Visibility", "Item_MRP", "Outlet_Establishment_Year"]
        ],
    )
)

X

# Train Test Split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=2529
)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Modeling

from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor(random_state=2529)

rfr.fit(X_train, y_train)

# Model Prediction

y_pred = rfr.predict(X_test)

y_pred.shape

y_pred

# Model Evaluation

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mean_squared_error(y_test, y_pred)

mean_absolute_error(y_test, y_pred)

r2_score(y_test, y_pred)


# Get Visualization of Actual vs Predicted Results

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Price vs Predicted Price")
plt.show()
