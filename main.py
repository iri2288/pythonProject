print(dir(''))
# Методы строк
# strip
# split
# join
# count

s = 'работа'
f = 'а'
if f in s:
    print('буква', f, 'есть в слове', s)
    print('и она встречается', s.count(f), 'раз(а)')
else:
    print('Буквы', f, 'в слове', s, 'нет!')

print('C:\\Windows\\Fonts') # запись пути
