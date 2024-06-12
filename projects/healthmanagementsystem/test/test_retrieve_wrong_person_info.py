import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the function to be tested
from ..src import health


class TestInputWrongPersonInfo(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_person_number(self, mock_stdout, mock_input):
        health.input_person_data(4)

        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid person number.")


if __name__ == '__main__':
    unittest.main()