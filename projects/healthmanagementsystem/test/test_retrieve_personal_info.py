import unittest
from unittest.mock import patch
from io import StringIO
from ..src import health


class TestRetrievePersonalInfo(unittest.TestCase):

    def test_retrieve_personal_info(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            health.retrieve_personal_info("anu")
            self.assertEqual(mock_stdout.getvalue(), "Gender: Female\nHeight: 160 cm\nWeight: 50 kg\n\n")

if __name__ == "__main__":
    unittest.main()
