# Квантификаторы (quantifier)
# m - минимальное число совпадений
# n - максимальное число совпадений
# {m} - ровно m раз
# {m,} - m раз  и более
# {, n} - не более n раз
# {m, n} - от m до n раз
import re

pattern = 'o{3,5}'  # в скобках пишетсяч без пробела
testString = 'Google, Gooogle, Goooooogle'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(result)

pattern = 'Go{3,}gle'  # версия написания Google с 3 'o' и более
testString = 'Google, Gooogle, Goooooogle'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(result)

pattern = 'Go{,2}gle'  # версия написания Google с 3 'o' и более
testString = 'Google, Gooogle, Goooooogle'

result = re.findall(pattern, testString, re.I)  # re.I игнорируя регистр
print(result)
