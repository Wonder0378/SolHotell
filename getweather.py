"""
Name: Marcus Hedquist
Date: 06-04-2022
Info:
<Insert information about file>
"""
import requests

class GetWeather:
    def __init__(self):

        #the api key can be used to access information about the wather anywhere in the world
        api_key = '647606470e7d8926da64ece5273d596b'

        #our hotell is located in the city Victoria so therefore the input is victoria
        input_ = ("Victoria")

        #data about the weather in Victoria is being collected from the open api
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={input_}&units=imperial&APPID={api_key}")

        #the variables is being set to the information
        self.weather = weather_data.json()['weather'][0]['main']
        self.temp = weather_data.json()['main']['temp']

        #translating the data from english to swedish
        if self.weather == ("Clear"):
            self.weather = ("Klart")
        elif self.weather == ("Clouds"):
            self.weather = ("Molnigt")

        #the temperature is getting recalculated from fahrenheit to celcuis
        self.temp2 = self.temp-32
        self.tempCelcius = round(self.temp2*0.5556)
        self.tempText = str(self.tempCelcius)