# Строки
# Исключения
# Модули и их применение
# Поиск строки
# Метод find(substr, start=0, end = None)

string = 'Видеть, петь'
if 'еть' in string:
    count = string.count('еть')
    print('"еть" встречается ', count, 'раз(а):')

if string.find('еть') != -1:
    count = string.count('еть')
    print('"еть" встречается ', count, 'раз(а):')

