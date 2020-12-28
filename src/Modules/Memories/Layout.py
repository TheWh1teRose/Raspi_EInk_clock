from Memories import Memories
from PIL import Image,ImageDraw,ImageFont

def listLayout(x,y,Himage, epd):
    draw = ImageDraw.Draw(Himage)
    font = ImageFont.truetype('Piboto-Light.ttf', 16)

    mem = Memories()

    nextMemories = mem.getNextThreeMemories()
    beforeAYearMemories = mem.getBeforAYear()
    row = 0
    for i in range(len(beforeAYearMemories)):
        draw.text((x + 10, y + row * 20), beforeAYearMemories[i]['name'], font=font, fill=0)
        draw.text((x + 160, y + row * 20), 'vor ' + str(beforeAYearMemories[i]['beforeYears']) + ' Jahren', font=font, fill=0)
        row += 1


    for i in range(min(len(nextMemories) ,3 - min( len(beforeAYearMemories), 3 ))):
        draw.text((x + 10, y + row*20), nextMemories[i]['name'], font=font, fill=0)
        draw.text((x + 160, y + row*20), 'in ' + str(nextMemories[i]['inDays']) + ' Tagen', font=font, fill=0)
        row += 1

def getLayout(name, x,y,Himage, epd):
    if name == 'list':
        listLayout(x,y,Himage, epd)




