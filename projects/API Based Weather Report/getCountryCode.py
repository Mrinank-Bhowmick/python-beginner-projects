"""
file_handler.py - A module for extracting a value from a JSON file based on a given key.

This module contains a function `extract_key_value_from_file` that retrieves a value from a JSON file
based on a given key.

Functions:
    extract_key_value_from_file(key): Extracts a value from a JSON file based on a given key.


"""

import json

def extract_key_value_from_file(key):
    """
    Extracts a value from a JSON file based on a given key.

    Parameters:
        key (str): The key for which the value needs to be retrieved from the JSON file.

    Returns:
        The corresponding value from the JSON file for the given key, or None if the key is not found.

    Raises:
        FileNotFoundError: If the specified JSON file cannot be found.
        json.JSONDecodeError: If the JSON file cannot be decoded.
    """
    try:
        # Open the JSON file in read mode
        with open("countryCode.json", 'r') as file:
            # Load JSON data from the file
            data = json.load(file)
            # Retrieve the value for the given key from the JSON data
            value = data.get(key)
            return value
    except FileNotFoundError as e:
        # Handle file not found error
        print("Error: File not found:", e)
        return None
    except json.JSONDecodeError as e:
        # Handle JSON decoding error
        print("Error: JSON decoding error:", e)
        return None
