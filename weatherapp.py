import requests
import json

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] != "404":
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_desc}")
    else:
        print("City not found.")


api_key = "30065fd0a9f4ecb51e7ccb8b350dc7ce"  #OpenWeatherMap API key
location = input("Enter city name or ZIP code: ")
weather_data = get_weather(api_key, location)
display_weather(weather_data)
