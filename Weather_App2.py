# Weather App:
# Build a script that displays the weather for a specified location using the pyowm module,
# allowing users to input a location and receive current weather information

import pyowm

location = input("Enter location: ")
owm = pyowm.OWM("your-api-key") # you must enter your api key here

observation = owm.weather_at_place(location)
weather = observation.get_weather()

temperature = weather.get_temperature("celsius")["temp"]
status = weather.get_detailed_status()

print(f"Current temperature in {location}: {temperature}°C")
print(f"Current weather status in {location}: {status}")
