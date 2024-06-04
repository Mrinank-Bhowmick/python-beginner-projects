import unittest
from weather_api import fetch_weather

class TestFetchWeather(unittest.TestCase):

    # Test case for successful weather data retrieval
    def test_successful_fetch(self):
        api_key = "e082b74fb59e29a4838166304b19c678"
        location = "Salem"
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertEqual(status_code, 200)
        #self.assertIsNotNone(weather_data)

    # Test case for invalid API key
    def test_invalid_api_key(self):
        api_key = "INVALID_API_KEY"
        location = "London"
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertEqual(status_code, 401)

    # Test case for invalid location
    def test_invalid_location(self):
        api_key = "e082b74fb59e29a4838166304b19c678"
        location = "InvalidCityName"
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertEqual(status_code, 404)

    # Test case for missing API key
    def test_missing_api_key(self):
        api_key = ""
        location = "London"
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertNotEqual(status_code, 200)

    # Test case for missing location
    def test_missing_location(self):
        api_key = "e082b74fb59e29a4838166304b19c678"
        location = ""
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertNotEqual(status_code, 200)

    # Test case for invalid API key and location
    def test_invalid_api_key_and_location(self):
        api_key = "INVALID_API_KEY"
        location = "InvalidCityName"
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertNotEqual(status_code, 200)

    # Test case for empty API key and location
    def test_empty_api_key_and_location(self):
        api_key = ""
        location = ""
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertNotEqual(status_code, 200)

    # Test case for invalid API key format
    def test_invalid_api_key_format(self):
        api_key = "INVALID_API_KEY_FORMAT"
        location = "London"
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertNotEqual(status_code, 200)

    # Test case for invalid location format
    def test_invalid_location_format(self):
        api_key = "e082b74fb59e29a4838166304b19c678"
        location = "InvalidCityName123"
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertNotEqual(status_code, 200)

    # Test case for valid location with special characters
    def test_valid_location_with_special_characters(self):
        api_key = "e082b74fb59e29a4838166304b19c678"
        location = "New%20York"
        status_code, weather_data = fetch_weather(api_key, location)
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
