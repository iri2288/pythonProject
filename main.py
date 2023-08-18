from datetime import datetime as d

raw_time = d.time(d.now())

# строка форматирования времени - strftime
# %H - часы в 24 часовом формате
# %M - часы в 24 часовом формате
# %S - часы в 24 часовом формате

print('на часах', raw_time.strftime('%H:%M'))

cur_hour = int(raw_time.strftime('%H'))

if cur_hour >= 6 and cur_hour < 12:
    print('Доброе утро')
elif cur_hour >= 12 and cur_hour < 18:
    print('Добрый день')
elif cur_hour >= 18 and cur_hour < 23:
    print('Добрый вечер')
else:
    print('Доброй ночи')