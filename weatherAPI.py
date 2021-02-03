import pyowm;
from pyowm.owm import OWM
from datetime import date


def getTemp():
    APIKEY = '93efb93eba9ab98330f5e1dd7fbc354a'
    owm = pyowm.OWM(APIKEY)
    weatherManager = owm.weather_manager()
    weatherTemp = weatherManager.weather_at_place('Moscow,RU').weather
    temp_dict_celsius = weatherTemp.temperature('celsius')
    return int(temp_dict_celsius.get('temp'))

def getDate():
    today = date.today()
    dater = today.strftime("%B %d, %Y")
    return str(dater)


def collectData():
    data = []
    data.append(getDate())
    data.append(getTemp())
    return data
