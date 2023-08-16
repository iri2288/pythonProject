#определили переменные
greeting = 'Привет'
name = 'Дмитрий'

#вывод на экран
print(greeting + ', ' + name)

count = 3 # счетчик попыток
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

