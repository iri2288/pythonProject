from datetime import datetime as d

raw_time = d.time(d.now())

# строка форматирования времени - strftime
# %H - часы в 24 часовом формате
# %M - часы в 24 часовом формате
# %S - часы в 24 часовом формате

print('на часах', raw_time.strftime('%H:%M'))

cur_hour = int(raw_time.strftime('%H'))

if 6 <= cur_hour < 12:
    print('Доброе утро')
elif 12 <= cur_hour < 18:
    print('Добрый день')
elif 18 <= cur_hour < 23:
    print('Добрый вечер')
else:
    print('Доброй ночи')

#  тернарный оператор условия

t = 20

print('Тепло') if t > 24 else print('Прохладно')
#  выражение при True <условие> else выражение при False
