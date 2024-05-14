# Weather App

This is a simple weather application built using Python's Tkinter library. It fetches current weather data for a specified city from the OpenWeatherMap API and displays the temperature, weather description, humidity, and wind speed.

## Features

- Allows the user to enter a city name.
- Retrieves real-time weather data for the entered city.
- Displays temperature in Celsius, weather description, humidity percentage, and wind speed.

## Requirements

- Python 3.x
- `tkinter` (Included with Python)
- `requests` library (Install using `pip install requests`)
- `Pillow` library (Install using `pip install Pillow`)

## Usage

1. Clone the repository or download the `weather_app.py` file.
2. Replace `'YOUR_API_KEY'` in the `API_KEY` variable with your valid OpenWeatherMap API key.
3. Run the `weather_app.py` script.
4. Enter the name of the city for which you want to get the weather information.
5. Click the "Get Weather" button to retrieve and display the weather data.

## Configuration

- Obtain an API key from [OpenWeatherMap](https://openweathermap.org/) by signing up for a free account.
- Replace `'YOUR_API_KEY'` with your actual API key in the `weather_app.py` script.

## Disclaimer

This application is a simple example and may require additional error handling or features for production use. Use it responsibly and refer to the OpenWeatherMap API documentation for more details on usage limits and guidelines.
