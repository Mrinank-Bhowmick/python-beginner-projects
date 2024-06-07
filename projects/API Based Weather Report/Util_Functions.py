from datetime import datetime, timedelta


def wind_degree_to_direction(str_wind_degree):
    """
    Convert wind degree to wind direction.

    :param str_wind_degree: str, Wind degree from API (0 to 360)
    :return: Wind direction as a string (e.g., N, NE, E, etc.)
    """
    # convert wind degree from str to int.
    try:
        wind_degree = int(str_wind_degree)
    except ValueError:
        return "API Wind Degree data format error!"

    directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
    ]
    index = int((wind_degree + 11.25) // 22.5) % 16
    return directions[index]


def unix_timestamp_to_localtime(str_unix_timestamp, str_timezone_offset_seconds):
    """
    Convert unix timestamp to localtime (for sunrise and sunset).

    :param str_unix_timestamp: str, Unix timestamp (e.g., "1717715516")
    :param str_timezone_offset_seconds: str, timezone offset in second (e.g., "28800" represents UTC+8)
    :return: local_time (e.g., "2024-06-07 07:11:56")
    """
    # Convert strings to integers
    try:
        unix_timestamp = int(str_unix_timestamp)
    except ValueError:
        return "API sunset/sunrise data format error!"

    try:
        timezone_offset_seconds = int(str_timezone_offset_seconds)
    except ValueError:
        return "API timezone data format error!"

    # Convert Unix timestamp to UTC datetime
    utc_time = datetime.utcfromtimestamp(unix_timestamp)

    # Apply timezone offset
    local_time = utc_time + timedelta(seconds=timezone_offset_seconds)

    return local_time.strftime('%Y-%m-%d %H:%M:%S')


def convert_temperature(str_temperature_kelvin, temperature_unit):
    """
    Convert temperature in Kelvin degree to Celsius degree or Fahrenheit degree based on second parameter .

    :param str_temperature_kelvin: str, temperature in Kelvin degree (e.g., "291.19")
    :param temperature_unit: str, "C" for Celsius, "F" for Fahrenheit
    :return: temperature (e.g., "21.07 °C" or "67.12 °F")
    """
    # Convert strings to integers
    try:
        temperature_k = float(str_temperature_kelvin)
    except ValueError:
        return "API temperature data format error!"

    # Validate temperature_unit
    unit = str(temperature_unit).upper()
    if not (unit == "C" or unit == "F"):
        return "Temperature unit must either be 'C' or be 'F'!"

    # Converting
    if unit == 'C':
        temperature_c = temperature_k - 273.15
        return f"{temperature_c:.2f} °C"

    if unit == 'F':
        temperature_f = temperature_k * 9 / 5 - 459.67
        return f"{temperature_f:.2f} °F"
