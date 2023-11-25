import unittest
from displayCalendar import user_validation
class Test(unittest.TestCase):
    def test_valid_input(self):
        year = 2023
        month = 5
        expected_output = (2023, 5)
        self.assertEqual(user_validation(year, month), expected_output)

    def test_invalid_input_string(self):
        year = 'a'
        month = 5
        expected_output = None
        self.assertEqual(user_validation(year, month), expected_output)

    def test_invalid_input_out_of_range(self):
        year = 2023
        month = 13
        expected_output = None
        self.assertEqual(user_validation(year, month), expected_output)


if __name__ == '__main__':
    unittest.main()





