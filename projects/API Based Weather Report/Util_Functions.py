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
