import unittest
from unittest.mock import patch
from ..src import health

class TestLogWrongEntry(unittest.TestCase):
    @patch('builtins.input', side_effect=['exercise', 'value'])
    @patch('builtins.print')
    def test_invalid_entry_type(self, mock_print, mock_input):
        health.log_entry("person", 3)

        mock_print.assert_called_once_with("Invalid entry type.")


if __name__ == '__main__':
    unittest.main()