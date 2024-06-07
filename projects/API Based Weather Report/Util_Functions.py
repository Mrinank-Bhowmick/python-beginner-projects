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
        return "API Wind Degree data error!"

    directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
    ]
    index = int((wind_degree + 11.25) // 22.5) % 16
    return directions[index]


def unix_timestamp_to_localtime(str_unix_timestamp, str_timezone_offset_seconds):
    """
    Convert wind degree to wind direction.

    :param str_unix_timestamp: str, Unix timestamp (e.g., "1717715516")
    :param str_timezone_offset_seconds: str, timezone offset in second (e.g., "28800" represents UTC+8)
    :return: local_time (e.g., "2024-06-07 07:11:56")
    """
    # Convert strings to integers
    unix_timestamp = int(str_unix_timestamp)
    timezone_offset_seconds = int(str_timezone_offset_seconds)

    # Convert Unix timestamp to UTC datetime
    utc_time = datetime.utcfromtimestamp(unix_timestamp)

    # Apply timezone offset
    local_time = utc_time + timedelta(seconds=timezone_offset_seconds)

    return local_time.strftime('%Y-%m-%d %H:%M:%S')
