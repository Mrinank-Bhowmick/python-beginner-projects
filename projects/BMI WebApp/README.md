# BMI WebApp

A small BMI calculator built with PyWebIO. It asks for height and weight in a browser form and reports the BMI along with a weight classification.

## Example

1. Run `python main.py`. PyWebIO opens a browser page with two input fields.
2. Enter your height in metres (e.g. `1.75`) and your weight in kilograms
   (e.g. `70`).
3. The page displays the result, for example:
   ```
   Your BMI is 22.857142857142858 and the person is : normal
   ```
4. Different weight ranges produce classifications such as "underweight",
   "overweight", or "severely obese".

## How to run on localhost

```
pip install pywebio
python main.py
```

## Dependencies

- pywebio
