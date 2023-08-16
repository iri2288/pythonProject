# определили переменные
greeting = 'Привет'
name = 'Дмитрий'

# вывод на экран
print(greeting + ', ' + name)

count = 3  # счетчик попыток
password = '123'
userchoice = ''

while True: # вечный цикл
    userchoice = input('Введите пароль: ')
    if password == userchoice:
        print('Доступ разрешен')
        break

    count -= 1 # декремент
    if count == 0:
        print('Попытки исчерпаны')
        break
    print('Пароль неверный. Попыток осталось - ' + str(count))

# str(x) - преобразование X  в строку
# int(x) - преобразование X  в целое
# float(x) - преобразование X в десятичную дробь

temperature = 39.7 # запятая недопустима при float
string = 'Температура - ' + str(temperature)+'\xB0C'
#  ASCII 11111111
#Unicode 2 байта
# Escape Sequence
# string+= ', это почти' + str(int(temperature)+1)
string+= ', это почти ' + str(round(temperature,0))+'\xB0C'

print(string)
# температура - 39.8, это почти 40

# Списки
array = []  # пустой список
array2 = list()  # пустой список через функцию list
array3 = [1, 2, 3, 4, 5]  # аналог массива типа int
list_4 = [36.6, 50, 'Температура']
index = 2

lenght = len(list_4)
print('Список длиной -', lenght)
print(list_4[index])

counter = 0
while count < lenght(list_4):
    print(list_4[counter])
    counter += 1

# Срез подчинятеся sss
# s - start, по умолчанию - ноль
# s - stop (не включительно)
# s - step, по умолчанию - 1

a = ['имя', 'бремя', 'стремя', 'знамя', 'пламя', 'племя']
print(list_4[0:len(list_4):2])  # вывод четных чисел списка
print(a[1:len(a):2])
print(a[::-1])  # вывод листа/строки наоборот


