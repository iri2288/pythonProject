# Анонимные функции лямбда - функции (lambda)


def power(a, b):
    return a ** b

my_power = lambda a, b: a ** b
print(my_power(2,4))

lst = [1, 2, 3, 4, 5]

lst2 = map(lambda a: a * 2, lst)
print(list(lst2))

lst = ['Иван', 'Петр', 'Сидор']

lst_name = map(lambda n: 'Привет, ' + n, lst)
print(list(lst_name))

lst = ['Иван', 'Петр', 'Сидор']
lst.sort(reverse=True, key=lambda x: x[2])
print(lst)
