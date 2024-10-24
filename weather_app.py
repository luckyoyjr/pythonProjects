import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = "********"  # Replace with your actual API key

    # Use the Current Weather Data API (free version)
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        if weather_data.get('cod') == 200:
            # Extract relevant weather information
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            weather_desc = weather_data['weather'][0]['description']

            # Display the weather information
            weather_info.set(f"City: {city}\nTemperature: {temp}°C\nFeels Like: {feels_like}°C\n "
                             f"Humidity: {humidity}%\nDescription: {weather_desc.capitalize()}")
        else:
            messagebox.showerror("Error", weather_data.get('message', 'City not found'))
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")

#GUI with Tkinter
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="lightblue")

title_label = tk.Label(root, text="Weather App 🌦️", font=("Poppins", 18, "bold"), bg="lightblue",
                       justify="center")
title_label.pack(pady=10)

city_label = tk.Label(root, text="City Name:", font=("Poppins", 14), bg="lightblue")
city_label.pack(pady=5)
city_entry = tk.Entry(root, width=30, font=("Poppins", 14))
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", font=("Poppins", 12, "bold"),
                          command=get_weather)
search_button.pack(pady=10)

weather_info = tk.StringVar()
weather_label = tk.Label(root, textvariable=weather_info, font=("Poppins", 14), bg="lightblue",
                         justify="left")
weather_label.pack(pady=10)

root.mainloop()