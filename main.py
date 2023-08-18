#  number = input('Введите число: ')
#  num_array = list(number)
#  sum = 0

#  for n in range(len(number)):
#  sum += int(n)

#  print(sum)
#  1 вариант
a = input('Ввод числа:')
a_lenght = len(a)

print('Число разрядов:', a_lenght)

s = 0 # переменная для вычисления суммы

for x in a:
    s += int(x)
print('Число разрядов:', s)


#  2 вариант
a = list(input('Ввод числа:'))
a_lenght = len(a)

print(dir(a))  # все методы объекта "a"

print('Число разрядов:', a_lenght)
print('До применения map-функции:', a)

a = map(int, a)  # функция высшего порядка, применяет функцию ко всем эл-там списка
a = list(a)

print('После применения map-функции:', a)

s = 0 # переменная для вычисления суммы

for x in a:
    s += x
print('Число разрядов:', s)

#  3 вариант

a = list(input('Ввод числа:'))
a_lenght = len(a)

a = map(int, a)

print('Число разрядов:', sum(a))