import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=["API_KEY", "London", "England"])
    @patch('main.fetch_weather', return_value=(200, {
        "main": {"temp": 280, "humidity": 80},
        "weather": [{"description": "Cloudy"}],
        "wind": {"speed": 4},
        "sys": {"country": "GB"}
    }))
    @patch('main.write_to_file')
    def test_main_success(self, mock_write_to_file, mock_fetch_weather, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue().strip()
            self.assertIn("Current temperature is:", output)
            self.assertIn("Current weather desc  :", output)
            self.assertIn("Current Humidity      :", output)
            self.assertIn("Current wind speed    :", output)
            self.assertIn("Country Code          :", output)
        mock_write_to_file.assert_called_once_with("London", {
            "main": {"temp": 280, "humidity": 80},
            "weather": [{"description": "Cloudy"}],
            "wind": {"speed": 4},
            "sys": {"country": "GB"}
        })

    @patch('builtins.input', side_effect=["API_KEY", "London", "England"])
    @patch('main.fetch_weather', return_value=(404, {"message": "City not found"}))
    def test_main_client_error(self, mock_fetch_weather, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue().strip()
            self.assertIn("Failed to fetch weather data. Client error: Status Code 404 , message : City not found", output)

    @patch('builtins.input', side_effect=["API_KEY", "London","England"])
    @patch('main.fetch_weather', return_value=(500, None))
    def test_main_server_error(self, mock_fetch_weather, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue().strip()
            self.assertIn("Failed to fetch weather data. Server error: Status Code 500", output)

if __name__ == '__main__':
    unittest.main()
