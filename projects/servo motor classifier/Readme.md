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

## How to run

```
pip install pandas numpy scikit-learn matplotlib
python main.py
```

## Dependencies

pandas, numpy, scikit-learn, matplotlib

## Pyodide-runnable

No — it downloads a CSV over the network with `pd.read_csv(<url>)` and renders a Matplotlib window, neither of which works in Pyodide.
