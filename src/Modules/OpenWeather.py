import os
import shutil
from pprint import pprint

import requests


class OpenWeather:
    apiKey = ""
    lon = None
    lat = None

    baseUrl = "https://api.openweathermap.org/data/2.5/onecall?"

    def __init__(self, apiKey, lon, lat):
        self.apiKey = apiKey
        self.lon = str(lon)
        self.lat = str(lat)

    def getCourentTemperatur(self):
        url = self.baseUrl + "lat=" + self.lat + "&lon=" + self.lon + "&appid=" + self.apiKey \
              + "&exclude=minutely,hourly,daily,alerts&units=metric"
        data = requests.get(url).json()
        pprint(data["current"]["weather"][0]["icon"])
        return {
            "temperature": data["current"]["temp"],
            "weather_icon": self.getWeatherIcon(data["current"]["weather"][0]["icon"])
        }

    def getWeatherIcon(self, icon_code):
        if os.path.isfile("../../Img/WeatherIcons"+icon_code+".png"):
            img = open("../../Img/WeatherIcons" + icon_code + ".png")
            return img
        else:
            url = "http://openweathermap.org/img/wn/" + icon_code + "@2x.png"
            resp = requests.get(url, stream=True)
            local_file = open("../../Img/WeatherIcons/01n.png", 'wb')
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)
            del resp
            return local_file