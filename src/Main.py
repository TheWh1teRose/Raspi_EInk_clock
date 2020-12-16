from src.ConfigLoader import ConfigLoader
from src.Modules.OpenWeather import OpenWeather


lon, lat = ConfigLoader().getWeatherCoordinats()
temp = OpenWeather(ConfigLoader().getWeatherApiKey(), lon, lat)
print(temp.getCourentTemperatur())