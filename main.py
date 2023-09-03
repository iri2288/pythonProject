# Строки
# Исключения
# Модули и их применение
# Поиск строки
# Метод replace(old, new, count = None)
# Форматирование строки - позволяет выводить строку в удобном формате
# Форматирование строки методом позиционных параметров format
# Форматирование строки placeholder formating
# Форматирование строки при помощи f - строки с python > 3.6
name = 'Виктор'
age = 9
height = 141.56

f_string = 'Имя: {0},\nвозраст: {1},\nрост: {2} см'.format(name, age, height)
print(f_string)

# Форматирование строки placeholder formating
f_string = 'Имя: {:20s},\nвозраст: {:3d},\nрост: {:.1f} см'.format(name, age, height)
print(f_string)

# Форматирование строки при помощи f - строки
f_string = f'Имя: {name},\nвозраст: {age // 2},\nрост: {int(height)} см'
print(f_string)

f_string = f'Имя: {name:30s},\nвозраст: {age // 2},\nрост: {height:.1f} см'
print(f_string)




