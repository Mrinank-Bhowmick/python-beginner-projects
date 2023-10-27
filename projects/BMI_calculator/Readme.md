# BMI Calculator

This Python script calculates Body Mass Index (BMI) based on a person's height and weight. It then interprets the BMI to provide a classification ranging from underweight to clinically obese.

## How to Use

1. Make sure you have Python installed on your system.

2. Clone or download the repository.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the script by executing the following command:

   ```bash
   python bmi_calculator.py
   ```

5. Follow the on-screen instructions to input your height (in meters) and weight (in kilograms).

6. The program will display your BMI and the corresponding classification.

## Code Structure

- `bmi_calculator.py`: The main Python script containing the BMI calculation and interpretation logic.
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
