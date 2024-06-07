import unittest
from unittest.mock import patch
from io import StringIO
from ..src import health


class TestLogEntry(unittest.TestCase):

    @patch('builtins.input', side_effect=["Test log entry"])
    def test_log_entry(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            health.log_entry("anu", 1)
            self.assertEqual(mock_stdout.getvalue(), "Written successfully\n")

if __name__ == "__main__":
    unittest.main()