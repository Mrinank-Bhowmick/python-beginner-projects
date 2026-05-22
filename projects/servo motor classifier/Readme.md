# Servo motor classifier

## Descirption

Servos are basic components of many machines. There are different classes of servo for different function and to classify them can be hard for people of non-technical background.It can be solved by using a tool that classifies the servo in their respective classes.

### Parameters Used:

- Motor type
- Screw
- Pgain
- Vgain

## Libraries Used:

- Numpy
- Pandas
- Scikit-learn

## Example

1. Run `python main.py`. The script downloads the Servo Mechanism dataset from GitHub.
2. It encodes the `Motor` and `Screw` columns (A–E mapped to 0–4) and trains a linear regression model on 70% of the data.
3. Predictions are made on the remaining 30% and evaluation metrics (MSE, MAE, R²) are printed to the console.
4. A scatter plot window opens showing actual vs. predicted class values.

## How to run on localhost

```
pip install pandas numpy scikit-learn matplotlib
python main.py
```

## Dependencies

pandas, numpy, scikit-learn, matplotlib
