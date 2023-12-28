# SkyCast 🌤️

SkyCast is a Python application that allows users to retrieve weather information for a specific location. It provides two main features: Today's Weather and Forecast Weather. Users can enter a city name, and based on their selection, they will get either the current weather or a weather forecast for the chosen location.

> You can check this webapp on https://skycast.streamlit.app/

## Features

### 1. Today's Weather
- Retrieve the current weather information for a specified city.
- Display data such as temperature, wind speed, cloud coverage, visibility, weather description, wind direction, UV index, and dew point.
- Visualize the data in a user-friendly interface.

### 2. Forecast Weather
- Get weather forecasts for a chosen city.
- Customize the number of days for the forecast.
- Display data including temperature, wind speed, cloud coverage, visibility, weather description, wind direction, UV index, and dew point for each day.
- Visualize the temperature forecast on a line chart.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mrinank-Bhowmick/python-beginner-projects.git
   ```

2. Change the directory to the project folder:

   ```bash
   cd python-beginner-projects/projects/Skycast
   ```

3. Obtain an API key from [Weatherbit](https://www.weatherbit.io/).

4. Open the `skycast.py` file and replace `your_api_key_here` with your Weatherbit API key:

   ```python
   self.api_key = "your_api_key_here"
   ```

5. Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the SkyCast app:

   ```bash
   streamlit run skycast.py
   ```

By following these steps, you'll be able to use SkyCast with your own Weatherbit API key.

## How to Use

1. Choose the weather option from the sidebar: "Today's Weather" or "Forecast Weather."

2. Enter the name of the city for which you want to retrieve weather information.

3. If you select "Today's Weather," you will get the current weather details for the chosen city.

4. If you select "Forecast Weather," specify the number of days for the weather forecast and view the forecasted data.

## Contributing

Contributions to SkyCast are welcome! Here are some ways you can contribute:

- Improve the user interface by enhancing the design and layout.
- Add new features or weather-related functionalities.
- Refactor the code for better performance and maintainability.
- Fix bugs and issues reported by users.

Thank you for your contributions to SkyCast! 🌤️