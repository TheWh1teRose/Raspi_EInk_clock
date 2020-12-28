#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
from os.path import dirname

from PIL import Image,ImageDraw,ImageFont
sys.path.append(dirname(__file__))
from OpenWeather import OpenWeather

def standartWeatherLayout(x,y, Himage, epd):
    draw = ImageDraw.Draw(Himage)
    font18 = ImageFont.truetype('Piboto-Bold.ttf', 18)
    weather = OpenWeather().getCourentTemperatur()

    icon = weather["weather_icon"]
    Himage.paste(icon, (x + 10, y - 10))
    draw.text((x + 30, y + 75), str(weather["temperature"])+u" °C", font=font18, fill=epd.GRAY3)

def getLayout(name, x,y,Himage, epd):
    if name == 'standart':
        standartWeatherLayout(x,y,Himage, epd)



