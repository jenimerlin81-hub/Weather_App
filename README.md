# Weather App with Live OpenWeather API

A Python-based CLI weather application that fetches real-time weather information for a city using the OpenWeather API.

## 📌 Project Overview

The Weather App connects Python with a real-world REST API to retrieve current weather information.

The user enters a city name, and the application fetches weather data such as temperature, humidity, weather condition, feels-like temperature, and wind speed.

## ✨ Features

* 🌍 Search weather by city
* 🌡️ Real-time temperature
* 💧 Humidity information
* 🌤️ Weather condition
* 🌡️ Feels-like temperature
* 💨 Wind speed
* 🔄 Continuous city search
* ⚠️ API and network error handling
* 🔐 API key stored securely using `.env`

## 🛠️ Technologies Used

* Python 3
* Requests
* OpenWeather API
* JSON
* python-dotenv
* REST API
* Command Line Interface

## 📂 Project Structure

```text
Weather_App/
│
├── weather_app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 📦 Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install requests python-dotenv
```

## 🔑 API Key Setup

Create a `.env` file in the project folder:

```text
OPENWEATHER_API_KEY=YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your OpenWeather API key.

Do not upload the `.env` file to GitHub.

## ▶️ How to Run

Run the application:

```bash
python weather_app.py
```

Enter a city name when prompted:

```text
Enter city name: Chennai
```

To exit:

```text
Enter city name: exit
```

## 💻 Sample Output

```text
================================
          WEATHER REPORT
================================

City: Chennai, IN
Temperature: 30°C
Feels Like: 34°C
Humidity: 70%
Weather: Clear Sky
Wind Speed: 4.2 m/s

================================
```

## 🔄 Application Flow

```text
User enters city
        ↓
Python sends API request
        ↓
OpenWeather API
        ↓
JSON response
        ↓
Python parses JSON
        ↓
Weather information displayed
```

## 🧠 Learning Outcomes

This project helps understand:

* REST API integration
* HTTP requests
* JSON response parsing
* Python dictionaries
* Environment variables
* API authentication
* Exception handling
* Real-world cloud API usage

## 🚀 Future Improvements

* Add 5-day weather forecast
* Add GUI using Tkinter
* Add weather icons
* Add Celsius/Fahrenheit selection
* Save search history
* Add multiple-city comparison
* Display sunrise and sunset time

## ⚠️ Security Note

Never share or upload your OpenWeather API key publicly. Keep the key inside the `.env` file and add `.env` to `.gitignore`.

## 👩‍💻 Author

**Jeni Merlin**

AI & Data Science Student

## 📄 License

This project is created for educational and learning purposes.
