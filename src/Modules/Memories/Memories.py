import yaml
import os
from datetime import datetime

class Memories:
    memories = None

    def __init__(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + '/memories.yaml') as file:
            self.memories = yaml.load(file, Loader=yaml.FullLoader)['memories']

    def getNextThreeMemories(self):
        memories = self.memories
        futureMemories = []
        for memory in memories:
            dateObject = datetime.strptime(memory['date'], '%d.%m.%y')
            if dateObject > datetime.now():
                memory['inDays'] = (dateObject-dateObject.now()).days
                futureMemories.append(memory)
        futureMemories.sort(key= lambda memory: datetime.strptime(memory['date'], '%d.%m.%y'))
        if len(futureMemories)>3:
            return futureMemories[0:3]
        else:
            return futureMemories

    def getBeforAYear(self):
        memories = self.memories
        beforAYearMemories = []
        now = datetime.now()
        for memory in memories:
            dateObject = datetime.strptime(memory['date'], '%d.%m.%y')
            if dateObject.year < now.year:
                if 'dateEnd' in memory:
                    endDateObject = datetime.strptime(memory['dateEnd'], '%d.%m.%y')
                    if dateObject.replace(year=now.year) < now and endDateObject.replace(year=now.year) > now:
                        memory['beforeYears'] = now.year - dateObject.year
                        beforAYearMemories.append(memory)
                else:
                    if dateObject.day == now.day and dateObject.month == now.month:
                        memory['beforeYears'] = now.year - dateObject.year
                        beforAYearMemories.append(memory)
        return beforAYearMemories
