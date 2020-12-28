from Modules.TimeLocal import Layout as timeLayout
from Modules.Weather import Layout as weatherLayout
from Modules.Memories import Layout as memoriesLayout

def getLayout(module, name, x, y, HImage, epd):
    if module == 'timeLocal':
        timeLayout.getLayout(name, x, y, HImage, epd)
    elif module == 'weather':
        weatherLayout.getLayout(name, x, y, HImage, epd)
    elif module == 'memories':
        memoriesLayout.getLayout(name, x, y, HImage, epd)