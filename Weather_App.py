# Weather App:
# Build a simple weather app that retrieves the weather data for a specified location using an API.

import requests


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=YOUR_API_KEY" # you must enter your api key here
    response = requests.get(url)
    data = response.json()
    description = data["weather"][0]['description']
    temp = data['main']['temp']
    return "The weather in " + city + " is " + description + " with a temperature of " + str(temp) + " degrees Celsius."


print(get_weather("London"))
