import unittest
from Util_Functions import (
    wind_degree_to_direction,
    unix_timestamp_to_localtime,
    convert_temperature,
)


class MyTestCase(unittest.TestCase):
    def test_wind_degree_to_direction(self):
        self.assertEqual("ENE", wind_degree_to_direction("60"))
        self.assertEqual("SE", wind_degree_to_direction("130"))
        self.assertEqual("W", wind_degree_to_direction("280"))

    def test_wind_degree_to_direction_parameter_format_error(self):
        self.assertEqual(
            "API Wind Degree data format error!", wind_degree_to_direction("abc")
        )

    def test_unix_timestamp_to_localtime(self):
        self.assertEqual(
            "2024-06-07 07:11:56", unix_timestamp_to_localtime("1717715516", "28800")
        )

    def test_unix_timestamp_to_localtime_unix_timestamp_format_error(self):
        self.assertEqual(
            "API sunset/sunrise data format error!",
            unix_timestamp_to_localtime("abc", "28800"),
        )

    def test_unix_timestamp_to_localtime_timezone_format_error(self):
        self.assertEqual(
            "API timezone data format error!",
            unix_timestamp_to_localtime("1717715516", "abc"),
        )

    def test_convert_temperature_to_celsius(self):
        self.assertEqual("15.44 °C", convert_temperature("288.59", "C"))

    def test_convert_temperature_to_fahrenheit(self):
        self.assertEqual("59.79 °F", convert_temperature("288.59", "F"))

    def test_convert_temperature_temperature_format_error(self):
        self.assertEqual(
            "API temperature data format error!", convert_temperature("abc", "F")
        )

    def test_convert_temperature_temperature_unit_error(self):
        self.assertEqual(
            "Temperature unit must either be 'C' or be 'F'!",
            convert_temperature("288.59", "H"),
        )


if __name__ == "__main__":
    unittest.main()
