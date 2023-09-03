# Исключения try+exept / try+finally
# Модули и их применение
n = 3
a = [1, 2]

if n<3:
    name = 'Федор'
try:
    # print(name)
    # print(a[5])
    with open('info.txt') as f:
        print(f.read())
except NameError:
    print('Имя не опрелелено')
except IndexError:
    print('индекс вне диапозона')
#except FileNotFoundError:
    print('файл не найден')
except Exception as exp:
    print('Тут вот какое дело:', exp)
    print('А имя исключения:', exp.__class__.__name__)  # можно узнать тип и имя исключения

try:
    pass  # пытаемся выполнить операции/ию, действия
except:
    pass  # прописываем обработчик исключения
else:
    pass  # если исключения не возникло
finally:
    pass  # выполняется в любом случае

print('Считаем остаток от деления числа 10')
num = input('Ввведите целое число')
at_the_end = ''

try:
    value = int(num)  # пытаемся преобразовать строку в целое число
    res = 10 % value
except ZeroDivisionError:  # деледение на ноль
    print('На ноль делить нельзя')
    at_the_end = 'Aй-Ай'
except ValueError:  # делдение на ноль
    print('Вас просили ыввести целое число.')
    print(f'А вот, что ввели Вы: {num}')
    at_the_end = 'Ну как же так?'
except Exception as e:
    print('Вот такое исключение', e.__class__.__name__)
    at_the_end = 'Вот еще что'
else:
    print(f'Остаток от деления 10 на {value} будет {res}')
    at_the_end = 'Спасибо!'
finally:
    print('Спасибо!')  # выполняется в любом случае


max_val = 10
min_val = 1
try:
    cur_val = int(input(f'Введите целое число от {min_val} до {max_val}'))
    if not min_val <= cur_val <= max_val:
        raise ValueError('Введенное число вне диапозона')
except ValueError as exep:
    print('Будьте внимательны:', exep)
else:
    print(f'Да, введенное число лежит в заданном диапозоне {min_val}...{max_val}')
