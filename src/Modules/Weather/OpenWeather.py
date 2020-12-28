import os
import shutil
from io import BytesIO

import numpy as np
import urllib2 as urllib
from StringIO import StringIO
from pprint import pprint

from ConfigLoader import ConfigLoader

import requests
from PIL import Image, ImageOps


class OpenWeather:
    apiKey = ""
    lon = None
    lat = None

    baseUrl = "https://api.openweathermap.org/data/2.5/onecall?"

    def __init__(self):
        self.apiKey = ConfigLoader().getWeatherApiKey()
        self.lon, self.lat = ConfigLoader().getWeatherCoordinats()

    def getCourentTemperatur(self):
        url = self.baseUrl + "lat=" + str(self.lat) + "&lon=" + str(self.lon) + "&appid=" + self.apiKey \
              + "&exclude=minutely,hourly,daily,alerts&units=metric"
        data = requests.get(url).json()
        pprint(data["current"]["weather"][0]["icon"])
        return {
            "temperature": data["current"]["temp"],
            "weather_icon": self.getWeatherIcon(data["current"]["weather"][0]["icon"])
        }

    def getWeatherIcon(self, icon_code):
        print(os.getcwd())
        img = Image.open('Modules/Weather/WeatherIcons/' + icon_code + '2x-ConvertImage.bmp').convert('L')
        return img