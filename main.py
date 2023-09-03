# Модули и их применение
#import lib as l

#if __name__ as '__main__':
    #l.sum(5, 5)

# from lib import *  перегружает пространство имен
# from lib import sum  перегружает пространство имен
# sum(5, 5)

import requests

key = 'dc3659c8cdf392c6f36d48a66fd18765'
city = input('Введите город: ')

# ссылка, с которой мы получим все данные в формате JSON
url = 'http://api.openweathermap.org/data/2.5/weather'
# Дополнительные параметры (Ключ, город введенный пользователем и единицы измерения - metric означает Цельсий)
params = {'APPID': key, 'q': city, 'units': 'metric'}

result = requests.get(url, params=params)
res = result.json()
print(res)
print('Температура:', res['main']['temp'], '°C')
print('Реально ощущается как:', res['main']['feels_like'], '°C')