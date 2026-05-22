# BMI Calculator

This Python script calculates Body Mass Index (BMI) based on a person's height and weight. It then interprets the BMI to provide a classification ranging from underweight to clinically obese.

## Example

```text
Here You can take the reference chart

╒════════════════╤═════════════════╕
│ BMI            │ Weight Status   │
╞════════════════╪═════════════════╡
│ Below 18.5     │ Underweight     │
│ 18.5 – 24.9    │ Normal weight   │
│ 25.0 – 29.9    │ Overweight      │
│ 30.0 and above │ Obese           │
╘════════════════╧═════════════════╛

Enter your height in meters: 1.75
Enter your weight in kilograms: 68
Your BMI is 22.2, you have a normal weight.
```

## How to Use

1. Make sure you have Python installed on your system.

2. Clone or download the repository.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the script by executing the following command:

   ```bash
   python "BMI calculator.py"
   ```

5. Follow the on-screen instructions to input your height (in meters) and weight (in kilograms).

6. The program will display your BMI and the corresponding classification.

## Code Structure

- `BMI calculator.py`: The main Python script containing the BMI calculation and interpretation logic.
- `README.md`: This file, providing an overview of the BMI calculator and usage instructions.

## Functions

### `calculate_bmi(height, weight)`

Calculate BMI given height (in meters) and weight (in kilograms).

- Parameters:
  - `height` (float): Height in meters.
  - `weight` (float): Weight in kilograms.

- Returns:
  - float: Calculated BMI.

### `interpret_bmi(bmi)`

Interpret the BMI and provide a classification.

- Parameters:
  - `bmi` (float): Calculated BMI.

- Returns:
  - str: BMI interpretation.

### `main()`

The main function to execute the BMI calculation and interpretation.

## Error Handling

The script handles invalid input, ensuring that only numerical values for height and weight are accepted.
