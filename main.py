import turtle as t

RND = 360 # 360 градусов в замкнутой фигуре
dist = 120  # дистанция
figs = 8 # число фигур
sides = 4  # число сторон
f_angle = RND / figs  # угол для наклона фигур
angle = RND / sides  # угол для сторон фигуры
fig_count = 0  # счетчик фигур
count = 0  # счетчик сторон

while fig_count < figs: # считаем фигуры
    count = 0 # обнуляем счетчик сторон
    while count < sides: # считаем строны фигур
        t.forward(dist)
        t.right(angle)
        count += 1
    fig_count += 1
    t.right(f_angle)

t.mainloop()

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

coffee = input('Сколько стоил кофе: ')
donut = input('Сколько стоил пончик: ')
print(type(coffee))
print('Вы потратили: ', int(coffee) + int(donut), 'руб.')

