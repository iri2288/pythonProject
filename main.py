#определили переменные
greeting = 'Привет'
name = 'Дмитрий'

#вывод на экран
print(greeting + ', ' + name)

a, b = 10, 3/5 # объявили 2 переменные

print(a, '+', b, '=', a + b) # оператор сложения
print(a, '-', b, '=', a - b) # оператор вычитания
print(a, '*', b, '=', a * b) # оператор умножения
print(a, '/', b, '=', a / b) # оператор деления результат всегда типа float
print(a, '//', b, '=', a // b) # оператор деления нацело
print('остаток от деления', a, 'на', b, '=', a % b) # оператор деления нацело
print(a, 'в степени', b, '=', a ** b) # оператор возведения в степень

a += 1 # инкремент (a = a + 1)
b -= 1 # декремент (b = b - 1)
