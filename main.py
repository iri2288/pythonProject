date_west = '2023-08-23'
# date_west_lst = date_west.split('-')[::-1]
# date_west = '.'.join(date_west_lst)
print('.'.join(date_west.split('-')[::-1]))

#  с помощью split и join удалить все пробелы
name = '  В ал ен ти н'
print(''.join(name.split()))

# Списочные выражения
# (list comprehension)

# классический способ заполнения списка
a = []
#for x in range(10):
   # a.append(x)
a = [x for x in range(10)]
print(a)