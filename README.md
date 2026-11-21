# 🌤️ Weather Data

A simple command-line weather app built with Python.

This is one of my first Python projects. I built it to practice working with APIs, handling JSON responses, and fetching data from external services.

Enter a city or country name, and the program will show you its current weather information!

## ✨ Features

- 🌍 **City Search** — Search for cities around the world.
- 🏳️ **Country Detection** — Automatically recognizes country names.
- 📍 **Capital Lookup** — If you enter a country, it automatically finds its capital and checks the weather there.
- 🌡️ **Temperature** — Get the current temperature in Celsius.
- 🥵 **Feels Like** — Check how warm or cold it actually feels.
- 💧 **Humidity** — View the current humidity percentage.
- 💨 **Wind Speed** — Check the current wind speed in km/h.

## 👀 Preview

**Searching for a country:**

```text
Enter a city or country name: Bangladesh

Bangladesh is a country.
The capital city is Dhaka.

Weather in Dhaka, Bangladesh:
Temperature: 24.0°C
Feels like: 27.5°C
Humidity: 88%
Wind Speed: 9.7 km/h
```

**Searching for a city:**

```text
Enter a city or country name: Dhaka

Weather in Dhaka, Bangladesh:
Temperature: 24.0°C
Feels like: 27.5°C
Humidity: 88%
Wind Speed: 9.7 km/h
```

*Example output. Actual weather values may vary.*

## 🛠️ Built With

- 🐍 Python
- 📦 Requests
- 🌐 Open-Meteo API
- 🌍 CountriesNow API

## 🚀 Getting Started

Want to try it out? Follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/syssamin/weather-data.git
```

### 2. Navigate to the project folder

```bash
cd weather-data
```

### 3. Install dependencies

```bash
pip install requests
```

### 4. Run the program

```bash
python main.py
```

Enter a city or country name and get its current weather!

## 🌐 APIs Used

This project uses the following APIs:

- 📍 [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) — Finds the geographical coordinates of a city.
- 🌤️ [Open-Meteo Weather API](https://open-meteo.com/en/docs) — Retrieves current weather information.
- 🏳️ [CountriesNow API](https://countriesnow.space/) — Identifies countries and retrieves their capital cities.

## 🔮 What's Next?

I'm still learning, and there's plenty of room to improve this project!

Some things I'd like to add:

- 🌧️ Weather descriptions (sunny, cloudy, rainy, etc.).
- 📅 Forecasts for upcoming days.
- ⚙️ Better error handling.
- 🖥️ A graphical user interface (GUI).

## 👨‍💻 About Me

I'm currently learning Python and building small projects to improve my programming skills.

This project is a small part of my learning journey. More projects coming soon!

**GitHub:** [@syssamin](https://github.com/syssamin)

---

⭐ Thanks for checking out my project! Feedback and suggestions are always welcome.