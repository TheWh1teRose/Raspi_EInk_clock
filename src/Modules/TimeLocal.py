from time import strftime, localtime

from src.ConfigLoader import ConfigLoader


class TimeLocal:
    timeformat = None

    def __init__(self):
        self.timeformat = ConfigLoader().getTimeFormat()

    def getTimeString(self):
        if self.timeformat == "24h":
            return strftime("%H:%M", localtime())
        elif self.timeformat == "12h":
            return strftime("%I:%M", localtime())

    def getDateString(self):
        return strftime("%d.%m.", localtime())
