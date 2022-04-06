"""
Name: Samuel Hellqvist
Date: 23-03-2022
Info:
This is a weather app that will display what weather it is somewhere in the world
"""

import requests

#api-nyckeln används för att få tillgång till data om vädret från hela världen
api_key = '647606470e7d8926da64ece5273d596b'

#vårat hotell ligger i staden Victoria på Sychellerna och därför är inputen Victoria
input_ = ("Victoria")

#data om vädret i Victoria hämtas
weather_data = requests.get(
     f"https://api.openweathermap.org/data/2.5/weather?q={input_}&units=imperial&APPID={api_key}")

#variabler sätts
weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']

#variablerna är annars på engelska men översätts här till svenska
if weather == ("Clear"):
     weather = ("Klart")
elif weather == ("Clouds"):
     weather = ("Molnigt")

#temperaturen räknas om från fahrenheit till celcius
temp2 = temp-32
tempCelcius = round(temp2*0.5556)

#hotellets väder redovisas för användaren
print("Vädret just nu på hotellet: ")
print(f"{tempCelcius}°C")
print(f"{weather}")