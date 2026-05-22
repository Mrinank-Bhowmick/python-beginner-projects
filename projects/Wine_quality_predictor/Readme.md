# Wine quality Predictor
## Descirption
During production of wine there may occur an reduction in quality due to some error in production process. Since wine is produced in large quantities this can result in wastage of wine. This problem can be simply solved using a tool that inputs various quality parameters of wine from previous batch and predict the quality of wine.
### Parameters Used:
- Fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulphur dioxide
- total sulphur dioxide
- density
- pH
- sulphates
- alchol
- quality

## Example

Running `python main.py` trains an SVM classifier on `WhiteWineQuality.csv` and prints a confusion matrix and classification report showing per-quality-class precision, recall, and F1 scores:

```text
[[  0   0   1   0   0   0]
 [  0   5  12   3   0   0]
 ...
 ]
              precision    recall  f1-score   support
           3       0.00      0.00      0.00         1
           4       0.45      0.25      0.32        20
           5       0.58      0.72      0.64       326
           6       0.55      0.54      0.55       399
           7       0.47      0.38      0.42       141
           8       0.33      0.08      0.13        37
```

## Libraries Used:
- Numpy
- Pandas
- Scikit-learn - Support Machine Vector
