import tabulate
import csv


def reference_chart():
    """
    This is a function used to tabulate the data
    of the BMI scale for the user. This requires a CSV file 'bmi.csv' and two libraries: "csv" and "tabulate".
    It won't take any arguments and won't return anything.
    """
    list2 = []
    with open("bmi.csv") as file1:
        list1 = csv.reader(file1)
        for line in list1:
            list2.append(line)
        print("Here you can take the reference chart:\n")
        print(tabulate.tabulate(list2[1:], headers=list2[0], tablefmt="fancy_grid"))


def calculate_bmi(height, weight):
    """
    Calculate BMI given height (in meters) and weight (in kilograms).

    Args:
        height (float): Height in meters.
        weight (float): Weight in kilograms.

    Returns:
        float: Calculated BMI.
    """
    try:
        bmi = round(weight / (height**2), 2)
        return bmi
    except ZeroDivisionError:
        return None


def interpret_bmi(bmi):
    """
    Interpret the BMI and provide a classification.

    Args:
        bmi (float): Calculated BMI.

    Returns:
        str: BMI interpretation.
    """
    if bmi is None:
        return "Invalid input. Height should be greater than 0."

    if bmi < 18.5:
        return f"Your BMI is {bmi}, you are underweight."
    elif bmi < 24.9:
        return f"Your BMI is {bmi}, you have a normal weight."
    elif bmi < 29.9:
        return f"Your BMI is {bmi}, you are overweight."
    elif bmi < 34.9:
        return f"Your BMI is {bmi}, you are obese (Class I)."
    elif bmi < 39.9:
        return f"Your BMI is {bmi}, you are obese (Class II)."
    else:
        return f"Your BMI is {bmi}, you are obese (Class III)."


def get_user_input():
    """
    Allow the user to enter height and weight in their preferred units.
    Returns height in meters and weight in kilograms.
    """
    try:
        unit_choice = input("Would you like to input height and weight in metric (meters/kg) or imperial (feet/inches/lbs)? (Enter 'metric' or 'imperial'): ").strip().lower()
        
        if unit_choice == "metric":
            height = float(input("Enter your height in meters: "))
            weight = float(input("Enter your weight in kilograms: "))
        
        elif unit_choice == "imperial":
            feet = float(input("Enter your height (feet): "))
            inches = float(input("Enter additional height (inches): "))
            height = (feet * 0.3048) + (inches * 0.0254)  # Convert to meters
            weight = float(input("Enter your weight in pounds: ")) * 0.453592  # Convert to kilograms
        
        else:
            print("Invalid choice. Please try again.")
            return None, None
        
        if height <= 0 or weight <= 0:
            print("Height and weight must be greater than 0. Please try again.")
            return None, None
        
        return height, weight

    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return None, None


def main():
    print("Welcome to the BMI Calculator!")
    print("This tool helps you calculate your Body Mass Index (BMI) and understand your health category.")
    print("------------------------------------------------------\n")
    
    reference_chart()
    
    height, weight = get_user_input()
    if height is None or weight is None:
        return

    bmi = calculate_bmi(height, weight)
    result = interpret_bmi(bmi)
    print(result)


if __name__ == "__main__":
    main()
