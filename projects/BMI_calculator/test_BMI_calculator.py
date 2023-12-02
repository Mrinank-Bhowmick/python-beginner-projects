import unittest
from BMI_calculator import calculate_bmi, interpret_bmi


class TestBMICalculator(unittest.TestCase):

    def test_calculate_bmi(self):
        height = 1.75
        weight = 70

        expected_bmi = 22.86
        actual_bmi = calculate_bmi(height, weight)
        self.assertEqual(actual_bmi, expected_bmi)

    def test_interpret_bmi_underweight(self):
        bmi = 17.5

        result = interpret_bmi(bmi)

        self.assertEqual(result, "Your BMI is 17.5, you are underweight.")


if __name__ == '__main__':
    unittest.main()
