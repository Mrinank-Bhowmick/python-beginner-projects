import unittest
from unittest.mock import patch
from io import StringIO
from ..src import health


class TestRetrieveEntry(unittest.TestCase):

    def test_no_records_found(self):
        # Simulate FileNotFoundError by mocking the open function
        with patch('builtins.open', side_effect=FileNotFoundError):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                health.retrieve_entry("Anna", 1)
                expected_output = "No records found for Anna's 1\n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()