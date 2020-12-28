import os
import sys
from os.path import dirname

from PIL import Image,ImageDraw,ImageFont
sys.path.append(dirname(__file__))
from TimeLocal import TimeLocal


def standartTimeDateLayout(x,y,Himage, epd):
    draw = ImageDraw.Draw(Himage)
    font60 = ImageFont.truetype('Piboto-Bold.ttf', 60)
    font18 = ImageFont.truetype('Piboto-Bold.ttf', 18)
    time = TimeLocal()

    draw.text((x+10, y+0), time.getTimeString(), font=font60, fill=0)
    draw.text((x+10, y+70), time.getDateString(), font=font18, fill=epd.GRAY3)

def getLayout(name, x,y,Himage, epd):
    if name == 'standart':
        standartTimeDateLayout(x,y,Himage, epd)



