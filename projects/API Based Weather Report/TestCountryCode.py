import unittest
from getCountryCode import extract_key_value_from_file
class TestExtractKeyValueFromFile(unittest.TestCase):
    def test_existing_key(self):
        # Assuming 'countryCode.json' contains valid data
        result = extract_key_value_from_file("usa")
        self.assertEqual(result, "US")

    def test_nonexistent_key(self):
        # Assuming 'countryCode.json' contains valid data
        result = extract_key_value_from_file("XYZ")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
