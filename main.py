# Регулярные выражения
import re

pattern = '[0-5][0-9]'  # отлавливается числа в этих пределах
testString = 'Время - 07:45'

result = re.findall(pattern, testString)
print(result)

# Группировка
# [есн] - в строке присутствует любой из этих символов
# [а-я] - в строке присутствует символ от а до я
# [а-яА-Я] - в строке присутствует символ от а до я и от А до Я
# [^абвгд] - ^ знак отрицания, все буквы кроме указанных

pattern = '[^абвгд]'  # любая буква в строке, кроме абвгд
testString = 'АБВГДейка - есть такая передача!'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(result)
print(*result, sep='')  # не списком

pattern = r'\((.+?)\)'  # извлекаем контекст, находящийся в скобках
testString = 'Поиск по образцу (это в скобках)'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(*result, sep='')  # не списком