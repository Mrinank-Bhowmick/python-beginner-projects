import unittest
from unittest.mock import patch
from io import StringIO

from ..src import health


class TestRetrieveWrongEntry(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_retrieve_wrong_entry(self, mock_stdout):
        health.retrieve_entry("Smith", 3)

        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid entry type.")


if __name__ == '__main__':
    unittest.main()