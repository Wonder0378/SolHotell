"""
Name: Marcus Hedquist
Date: 06-04-2022
Info:
<Insert information about file>
"""
import requests

class GetWeather:
    def __init__(self):

        #api-nyckeln används för att få tillgång till data om vädret från hela världen
        api_key = '647606470e7d8926da64ece5273d596b'

        #vårat hotell ligger i staden Victoria på Sychellerna och därför är inputen Victoria
        input_ = ("Victoria")

        #data om vädret i Victoria hämtas
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={input_}&units=imperial&APPID={api_key}")

        #variabler sätts
        self.weather = weather_data.json()['weather'][0]['main']
        self.temp = weather_data.json()['main']['temp']

        #variablerna är annars på engelska men översätts här till svenska
        if self.weather == ("Clear"):
            self.weather = ("Klart")
        elif self.weather == ("Clouds"):
            self.weather = ("Molnigt")

        #temperaturen räknas om från fahrenheit till celcius
        self.temp2 = self.temp-32
        self.tempCelcius = round(self.temp2*0.5556)
        self.tempText = str(self.tempCelcius)