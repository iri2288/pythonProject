# Регулярные выражения
#

import re

pattern = r'\b\w{4}\b'
pattern = r'\d'  # есть ли в строке цифры
testString = 'Для экстренных вызовов - 112'

result = re.search(pattern, testString)
# print(result)
print('Цифры присутствуют в строке') if result else print('Цифр нет!')

pattern = r'\d{3}'  # есть ли в строке 3 цифры идущие подряд
testString = 'Для экстренных вызовов - 112'

result = re.search(pattern, testString)
result = re.findall(pattern, testString)
print(result)
# print('Цифры присутствуют в строке') if result else print('Цифр нет!')

pattern = r'начать\Z'  # на что заканчивается
testString = 'Главное в любом деле - начать'

result = re.search(pattern, testString)
# print(result)
print('Цифры присутствуют в строке') if result else print('Цифр нет!')
