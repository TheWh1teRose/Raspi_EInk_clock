from src.ConfigLoader import ConfigLoader

config = ConfigLoader("example_config.yaml")
print(config.getTimeZone())