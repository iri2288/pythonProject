a = list(input('Ввод числа:'))

for n in a:
    if int(n) % 2 == 0:
        print('Число:', n, 'четное.')
    else:
        print('Число:', n, 'нечетное.')