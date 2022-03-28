"""
Name: Samuel Hellqvist
Date: 23-03-2022
Info:
This is a weather app that will display what weather it is somewhere in the world
"""

import requests

api_key = '647606470e7d8926da64ece5273d596b'

user_input = input("Enter city: ")

weather_data = requests.get(
     f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']

temp2 = temp-32
tempCelcius = round(temp2*0.5556)

print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {tempCelcius}°C")