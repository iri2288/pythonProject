# Квантификаторы (quantifier)
# m - минимальное число совпадений
# n - максимальное число совпадений
# {m} - ровно m раз
# {m,} - m раз  и более
# {, n} - не более n раз
# {m, n} - от m до n раз
# . - любой символ
# * - от нуля до "бесконечности" (32767) 2 байтовый int {0,}
# ? - от единицы до "бесконечности" (32767) 2 байтовый int {1,}
import re

pattern = r'<img.*>'  # greedy (жадный квантификатор)
testString = 'Картинка <img src="bg.jpg"> в тексте </p>'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(result)

pattern = r'<img.*?>'  # minor (не жадный квантификатор)
testString = 'Картинка <img src="bg.jpg"> в тексте </p>'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(result)


pattern = r'<img[^>]+src="([^">]+)"'  # вычленяем само название файла картинки
testString = 'Картинка <img src="bg.jpg"> в тексте </p>'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(result[0])

# в html - документе вытащить, находящееся между <p> и </p>
pattern = r'<p>(.*?)</p>'  # вычленяем само название файла картинки
testString = '<b>Жирный </b>.<p>Содержимое абзаца 2</p>.<i>курсив</i>'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(result[0])

# игнорируя от <p и до >
pattern = r'<p[^>]*>(.*?)</p>'  # вычленяем само название файла картинки
testString = '<b>Центрируем: </b><p align="center">Содержимое абзаца </p>'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(result[0])

# в html вытащить url из текста
pattern = r'http(?:s)?://[\S]+'  # вычленяем сайт для http
testString = 'Информация есть на сайте http://google.com'

result = re.findall(pattern, testString)  # re.I игнорируя регистр
print(result[0])

# https://regex101.com/
# в html вытащить anchor из тега ссылки
pattern = r'href=[\'"]?([^\'">]+)'  # вычленяем сайт для http
testString = '<a href="http://ya.ru">Яндекс</a>'

result = re.findall(pattern, testString)  # re.I игнорируя регистр
print(result[0])

# в html вытащить anchor из тега ссылки
pattern = r'<a.*?>(.*?)</a>'  # вычленяем сайт для http
testString = '<a href="http://ya.ru">Яндекс</a>'

result = re.findall(pattern, testString)  # re.I игнорируя регистр
print(result[0])
