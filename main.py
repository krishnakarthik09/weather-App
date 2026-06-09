import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your OpenWeatherMap API Key
API_KEY = "c683ef80ab498ae06532782846fdd278"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Warning", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:

            weather_info = f"""
City: {data['name']}
Country: {data['sys']['country']}

Temperature: {data['main']['temp']} °C
Feels Like: {data['main']['feels_like']} °C

Weather: {data['weather'][0]['main']}
Description: {data['weather'][0]['description']}

Humidity: {data['main']['humidity']} %
Pressure: {data['main']['pressure']} hPa

Wind Speed: {data['wind']['speed']} m/s

Visibility: {data['visibility']} meters

Latitude: {data['coord']['lat']}
Longitude: {data['coord']['lon']}
"""
            result_label.config(text=weather_info)

        else:
            result_label.config(text="City not found!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main Window
root = tk.Tk()
root.title("Weather App")
root.geometry("500x550")

# Heading
title = tk.Label(
    root,
    text="Weather Application",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# City Input
city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25
)
city_entry.pack(pady=10)

# Button
search_btn = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    command=get_weather
)
search_btn.pack(pady=10)

# Result Area
result_label = tk.Label(
    root,
    text="Enter a city name",
    justify="left",
    font=("Arial", 11)
)
result_label.pack(pady=20)

root.mainloop()