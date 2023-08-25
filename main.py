# Функции, количество аргументов должно совпадать, последовательность аргументов имеет значение
# Область внутри функции local scope
# Функция по умолчанию не имеет права работать с внешней глобальной областью данных,только если специально задать global
def greeting(name) -> str:  # определение типа
    # print('Привет', name)
    return 'Привет, ' + str(name)

result = greeting('Tim')
# greeting('Тимоша')
print(result)

def greeting(name, surname, age):
    # print('Привет', name)
    string = 'Привет, ' + str(name) + ' ' + str(surname) + '!'
    string += '\nТебе' + ' ' + str(age) + ' ' + 'лет'
    return string

result = greeting('Tim', 'Cat', 2)
print(result)

def greeting(name='Noname', surname='Nosurname', age=0):  # функция стала универсальной, если в первом аргументе задан
# параметр, остальные параметры также должны быть заданы
    # print('Привет', name)
    string = 'Привет, ' + str(name) + ' ' + str(surname) + '!'
    if age != 0:
        string += '\nТебе' + ' ' + str(age) + ' ' + 'лет'
    return string

result = greeting('Tim', 'Cat', 2)
result = greeting(surname='Tim', name='Cat')  # для изменения последовательности аргументов, вызов функции с именованным
# аргументами
print(result)

def greeting(name=' ', surname=' ', age=0, sex=' '):  # функция стала универсальной, если в первом аргументе задан
# параметр, остальные параметры также должны быть заданы
    # print('Привет', name)
    string = 'Привет, ' + str(name) + ' ' + str(surname) + '!'
    if age != 0:
        string += '\nТебе' + ' ' + str(age) + ' ' + 'лет'
    if sex:
        string+=  '\nПол' + sex
    return string

result = greeting('Tim', 'Cat', 2)
result = greeting(surname='Tim', name='Cat')  # для изменения последовательности аргументов, вызов функции с именованным
# аргументами
print(result)

def incr(number):
    # local scope
    return number + 1

# global scope
num = 5 # глобальная переменная
print(incr(num))

def incr():
    # local scope
    global num  #
    num +=1
    return num

# global scope
num = 5 # глобальная переменная
print(incr())
print(num)


def even_or_odd(number):
    if number % 2 == 0:
        return 'Четное'
    # else: не сработает т.к. функция закончится на return в условии if
    return 'Нечетное'

num = 6
print(even_or_odd(num))

