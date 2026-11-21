import requests

# This function takes a country name as input and returns the capital city of that country using the REST Countries API.



def get_country_capital(country_name):

    # API URL for finding a country's capital
    country_url = "https://countriesnow.space/api/v0.1/countries/capital/q"

    
    country_params = {
        "country": country_name
    }

    response = requests.get(
        country_url,
        params=country_params,
        timeout=10
    )

    if response.status_code == 404:
        return None

    response.raise_for_status()
    
    country_data = response.json()
    
    if country_data.get("error"):
        return None

    
    country_info = country_data.get("data")


    if not country_info:
        return None

  
    return country_info.get("capital")




# This is our main weather funciton

def get_weather(city_name):
    city_name = city_name.strip()

    if not city_name:
        print("Please enter a city or country name.")
        return

    try:
        capital_city = get_country_capital(city_name)


    except requests.RequestException:
        print("Could not check country information")
        return
    

    if capital_city:
        print(f"\n{city_name.title()} is a country.")
        print(f"The capital city is {capital_city}.")

        city_name = capital_city


    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    try:
        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )

        geo_response.raise_for_status()
        geo_data = geo_response.json()

    except requests.RequestException:
        print("Could not get weather data.")
        return

    if "results" not in geo_data:
        print(f"Could not get weather data.")
        return


    location = geo_data["results"][0]

    lat = location["latitude"]
    lon = location["longitude"]

    full_name = f"{location['name']}, {location.get('country', '')}"

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m"
    }

    try:
        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

    except requests.RequestException:
        print("Could not get weather data.")
        return

    current = weather_data["current"]

    print(f"\nWeather in {full_name}:")
    print(f"Temperature: {current['temperature_2m']}°C")
    print(f"Feels like: {current['apparent_temperature']}°C")
    print(f"Humidity: {current['relative_humidity_2m']}%")
    print(f"Wind Speed: {current['wind_speed_10m']} km/h")


if __name__ == "__main__":
        city = input("Enter a city or country name: ")
        get_weather(city)