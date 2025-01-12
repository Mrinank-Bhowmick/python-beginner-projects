import unittest
from unittest.mock import patch
from io import StringIO
from ..src import health


class TestLogPersonalInfo(unittest.TestCase):

    @patch('builtins.input', side_effect=["Female", "160", "50"])
    def test_log_personal_info(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            health.log_personal_info("anu")
            self.assertEqual(mock_stdout.getvalue(), "Personal information logged successfully\n")

if __name__ == "__main__":
    unittest.main()
