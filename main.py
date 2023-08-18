lst = ['божество', 'вдохновенье', 'смех', 'слезы', 'любовь']

# print('И', ', и '.join(lst))
string = 'И ' + ', и '.join(lst) + '.'
print(string)

print('И ', end='')
print(*lst, sep=', и ', end='.')