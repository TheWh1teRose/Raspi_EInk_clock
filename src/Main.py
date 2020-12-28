#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import time
import yaml
from datetime import datetime
from lib.waveshare_epd import epd2in7
from PIL import Image,ImageDraw,ImageFont
from Modules.TimeLocal import Layout as timeLayout
from Modules.Weather import Layout as weatherLayout
from Modules.Memories import Layout as memoriesLayout
from Modules import getLayout
from gpiozero import Button

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

logging.basicConfig(level=logging.DEBUG)

layouts = None
selectedLayout = 1

with open("../layouts.yaml") as file:
    layouts = yaml.load(file, Loader=yaml.FullLoader)

logging.info("epd2in7 Demo")
epd = epd2in7.EPD()
logging.info("init and Clear")

def refreshDisplay():
    epd.init()
    epd.Init_4Gray()
    epd.Clear(0xFF)
    Himage = Image.new('L', (epd.height, epd.width), 255)  # 255: clear the frame

    lastTimeClockRefresh = datetime.now()
    print(str(selectedLayout))
    for layout in layouts[selectedLayout]:
        getLayout(layout['module'], layout['layout'], layout['x'], layout['y'], Himage, epd)

    epd.display_4Gray(epd.getbuffer_4Gray(Himage.transpose(Image.FLIP_LEFT_RIGHT)))
    epd.sleep()

btn1 = Button(5)
btn2 = Button(6)
btn3 = Button(13)
btn4 = Button(19)

def handleBtn(btn):
    global selectedLayout
    pinNum = btn.pin.number
    switcher = {
            5: 1,
            6: 2,
            13: 1,
            19: 1
        }
    if selectedLayout is not switcher.get(pinNum, 1):
        selectedLayout = switcher.get(pinNum, 1)
        refreshDisplay()

btn1.when_pressed = handleBtn
btn2.when_pressed = handleBtn
btn3.when_pressed = handleBtn
btn4.when_pressed = handleBtn

try:
    while True:
        refreshDisplay()
        time.sleep(60)
except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()





