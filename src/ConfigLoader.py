import yaml


class ConfigLoader:
    yamlObject = None

    def __init__(self, config_file_name):
        with open("../" + config_file_name) as file:
            self.yamlObject = yaml.load(file, Loader=yaml.FullLoader)

    def getTimeZone(self):
        return self.yamlObject["timezone"]
