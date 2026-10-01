import os
import requests
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
from datetime import datetime


# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_current_weather(city):
    """Fetch current weather data."""

    if not API_KEY:
        return None, "API key not found. Check your .env file."

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            CURRENT_WEATHER_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 401:
            return None, "Invalid or inactive API key."

        if response.status_code == 404:
            return None, "City not found."

        response.raise_for_status()

        return response.json(), None

    except requests.exceptions.Timeout:
        return None, "Request timed out."

    except requests.exceptions.ConnectionError:
        return None, "Internet connection error."

    except requests.exceptions.RequestException as error:
        return None, f"API request failed: {error}"


def get_forecast(city):
    """Fetch 5-day forecast data."""

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            FORECAST_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 401:
            return None, "Invalid or inactive API key."

        if response.status_code == 404:
            return None, "City not found."

        response.raise_for_status()

        return response.json(), None

    except requests.exceptions.Timeout:
        return None, "Forecast request timed out."

    except requests.exceptions.ConnectionError:
        return None, "Internet connection error."

    except requests.exceptions.RequestException as error:
        return None, f"Forecast request failed: {error}"


def display_weather():
    """Get city weather and display it."""

    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning(
            "Input Required",
            "Please enter a city name."
        )
        return

    status_label.config(text="Fetching weather data...")
    root.update()

    current_data, current_error = get_current_weather(city)

    if current_error:
        status_label.config(text="Unable to fetch weather.")
        messagebox.showerror("Weather Error", current_error)
        return

    forecast_data, forecast_error = get_forecast(city)

    if forecast_error:
        status_label.config(text="Unable to fetch forecast.")
        messagebox.showerror("Forecast Error", forecast_error)
        return

    # Current weather data
    city_name = current_data["name"]
    country = current_data["sys"]["country"]

    temperature = current_data["main"]["temp"]
    feels_like = current_data["main"]["feels_like"]
    humidity = current_data["main"]["humidity"]

    weather_description = current_data["weather"][0]["description"]
    wind_speed = current_data["wind"]["speed"]

    current_text = (
        f"📍 {city_name}, {country}\n\n"
        f"🌡 Temperature : {temperature:.1f} °C\n"
        f"🌡 Feels Like  : {feels_like:.1f} °C\n"
        f"💧 Humidity    : {humidity}%\n"
        f"☁ Weather     : {weather_description.title()}\n"
        f"💨 Wind Speed  : {wind_speed} m/s"
    )

    current_label.config(text=current_text)

    # Forecast
    forecast_text = ""

    forecast_list = forecast_data["list"]

    # Display selected forecast entries
    for item in forecast_list[:8]:
        date_time = datetime.strptime(
            item["dt_txt"],
            "%Y-%m-%d %H:%M:%S"
        )

        temperature = item["main"]["temp"]
        humidity = item["main"]["humidity"]
        description = item["weather"][0]["description"]

        forecast_text += (
            f"{date_time.strftime('%d-%m %H:%M')}  |  "
            f"{temperature:.1f}°C  |  "
            f"{description.title()}  |  "
            f"Humidity: {humidity}%\n"
        )

    forecast_label.config(text=forecast_text)

    status_label.config(
        text=f"Weather updated for {city_name}"
    )


def clear_data():
    """Clear the weather information."""

    city_entry.delete(0, tk.END)

    current_label.config(
        text="Current weather will appear here."
    )

    forecast_label.config(
        text="Forecast will appear here."
    )

    status_label.config(text="Ready")


# -----------------------------
# Tkinter Window
# -----------------------------

root = tk.Tk()

root.title("Weather App - OpenWeather API")
root.geometry("750x650")
root.resizable(False, False)

# Main heading
title_label = tk.Label(
    root,
    text="🌤 Weather App",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=20)

# Search frame
search_frame = tk.Frame(root)

search_frame.pack(pady=10)

city_entry = tk.Entry(
    search_frame,
    width=30,
    font=("Arial", 14)
)

city_entry.grid(
    row=0,
    column=0,
    padx=10
)

search_button = tk.Button(
    search_frame,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    command=display_weather
)

search_button.grid(
    row=0,
    column=1,
    padx=5
)

clear_button = tk.Button(
    search_frame,
    text="Clear",
    font=("Arial", 12),
    command=clear_data
)

clear_button.grid(
    row=0,
    column=2,
    padx=5
)

# Current weather heading
current_heading = tk.Label(
    root,
    text="Current Weather",
    font=("Arial", 18, "bold")
)

current_heading.pack(pady=(20, 5))

# Current weather display
current_label = tk.Label(
    root,
    text="Current weather will appear here.",
    font=("Arial", 13),
    justify="left"
)

current_label.pack(pady=10)

# Forecast heading
forecast_heading = tk.Label(
    root,
    text="Forecast",
    font=("Arial", 18, "bold")
)

forecast_heading.pack(pady=(20, 5))

# Forecast display
forecast_label = tk.Label(
    root,
    text="Forecast will appear here.",
    font=("Consolas", 11),
    justify="left"
)

forecast_label.pack(pady=10)

# Status
status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 10)
)

status_label.pack(
    side="bottom",
    pady=15
)

# Run application
root.mainloop()