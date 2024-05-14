import tkinter as tk
import requests
from PIL import Image, ImageTk

API_KEY = '13cd40e26f7dcc88cfc08e3bd43da1fc'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    try:
        request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
        response = requests.get(request_url)
        weather_data = response.json()

        if response.status_code == 200:
            temperature_kelvin = weather_data['main']['temp']
            temperature_celsius = temperature_kelvin - 273.15
            weather_description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            # Update the result label with weather information
            result_text = (
                f"Temperature: {temperature_celsius:.2f}°C\n"
                f"Weather: {weather_description}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            result_label.config(text=result_text)


        else:
            result_label.config(text=f"Failed to retrieve weather data. Error {response.status_code}")
    except Exception as e:
        result_label.config(text=f"An error occurred: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("Weather App")
root.geometry('350x300')

label = tk.Label(root, text="Enter city name:")
label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

submit_button = tk.Button(root, text="Get Weather", command=lambda: get_weather(city_entry.get()))
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)

root.mainloop()
