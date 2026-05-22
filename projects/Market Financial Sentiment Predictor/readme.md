# Market Financial Sentiment Predictor

## Descirption

All day various news about companies comes and not all people can track this news. Due to this they can miss great investment opportinities or they can avoid risky situations thus saving them from losses.This tool solves this problem by analyzing financial news and then predicting the stock price.

## Libraries Used:

- Numpy
- Pandas
- Scikit-learn

## Example

```text
              precision    recall  f1-score   support

           0       0.85      0.82      0.84       130
           1       0.83      0.86      0.84       130

    accuracy                           0.84       260
   macro avg       0.84      0.84      0.84       260
weighted avg       0.84      0.84      0.84       260
```

The script loads `Financial Market News.csv`, trains a Random Forest classifier on the top-25 daily headlines, and prints a classification report showing sentiment prediction accuracy.

## How to run on localhost

```
pip install numpy pandas scikit-learn
python main.py
```

Requires the bundled `Financial Market News.csv` dataset.
