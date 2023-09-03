# Строки
# Исключения
# Модули и их применение
# Поиск строки
# Метод replace(old, new, count = None)
# Форматирование строки - позволяет выводить строку в удобном формате
# %s - строка, %f - дробь, %d - целое placeholder

string = '+7-812-345-67-89'
lenght = len(string)

# заменить дефис на пробел

spaced_phone = string.replace('-', ' ') # новая переменная тк строка неизменяемый тип данных
print(spaced_phone)

open_braked_phone = string.replace('-', ' (', 1)
close_braked_phone = open_braked_phone.replace('-', ') ', 1)
print(close_braked_phone)

tv = 'тиливизор'  # телевизор
write_tv = tv.replace('и', 'е', 2)
print(write_tv)

# Форматирование строки
name = 'Виктор'
age = 9
height = 141.56

f_string = '%15s,\nвозраст: %d лет,\nрост: %6.1f см' % (name, age, height)
print(f_string)  # 1f в росте округление


