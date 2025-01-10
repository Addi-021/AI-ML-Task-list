import requests

# Open-Meteo API URL for weather data
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 19.0760,  # Mumabi City latitude
    "longitude": 72.8777,  # Mumbai City longitude
    "current_weather": True,
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()

    # Parse the JSON response
    weather = response.json()["current_weather"]

    # Display specific information
    print("Current Weather in Mumbai City:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Wind Speed: {weather['windspeed']} km/h")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from the API: {e}")

