import yaml


class ConfigLoader:
    yamlObject = None

    def __init__(self):
        with open("../config.yaml") as file:
            self.yamlObject = yaml.load(file, Loader=yaml.FullLoader)

    def getTimeFormat(self):
        return self.yamlObject["timeformat"]

    def getWeatherApiKey(self):
        return self.yamlObject["weather"]["api-key"]

    def getWeatherCoordinats(self):
        return self.yamlObject["weather"]["lon"], self.yamlObject["weather"]["lat"]
