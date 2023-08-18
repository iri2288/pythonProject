lst = ['божество', 'вдохновенье', 'смех', 'слезы', 'любовь']

# print('И', ', и '.join(lst))
string = 'И ' + ', и '.join(lst) + '.'
print(string)

print('И ', end='')
print(*lst, sep=', и ', end='.')

# strip удаляет элементы в начале и конце строки
r = 'ротор'
print(r.strip('р'))
print(r.rstrip('р')) # удаляет только справа
print(r.lstrip('р')) # удаляет только слева