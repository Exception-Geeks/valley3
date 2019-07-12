import requests

def weather_info(city,units):
    if units=='imperial' or 'metric':
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=3124d86fcce638f1bf6490d191b7fc9e&units={units}'

    else:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=3124d86fcce638f1bf6490d191b7fc9e'

    res = requests.get(url).json()
    return res