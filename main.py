import requests

def get_weather(city_name):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }


    geo_respone = requests.get(geo_url, params=geo_params).json()


    if "results" not in geo_respone:
        print(f"Could not get weather data.")
        return 

    
    location = geo_respone["results"][0]


    lat = location["latitude"]
    lon = location["longitude"]

    full_name = f"{location['name']}, {location.get('country', '')}"

    weather_url = "https://api.open-meteo.com/v1/forecast"


    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m"
        
    }



    weather_response = requests.get(weather_url,params=weather_params).json()
    current = weather_response["current"]


    print(f"\nWeather in {full_name}:")
    print(f"Temperature: {current['temperature_2m']}°C (Feels like {current['apparent_temperature']})°C")


    print(f"Humidity: {current['relative_humidity_2m']}%")
    print(f"Wind Speed: {current['wind_speed_10m']} km/h")


if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)