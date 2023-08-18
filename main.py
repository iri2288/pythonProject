color = input('Цвет шарика: ')

if color == 'red' or color == 'blue':
    print('Buy ball')
else:
    print('Don*t buy ball')

match color:                        # работает с версии python 3.10
    case 'red' | 'blue':
        print('Buy ball')
    case _:
        print('Don*t buy ball')