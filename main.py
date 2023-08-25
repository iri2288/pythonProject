# множества исключает повторы
lst = [3, 1, 5, 3, 2, 4, 3, 2, 5, 3, 4]
num_set = set(lst)
print(num_set)  # для чисел упорядочивает

lst = ['3', '1', '5', '3', '2', '4', '3', '2', '5', '3', '4']
num_set = set(lst)
print(num_set)

a = {1, 2, 3, 4}
b = {2, 3, 5, 7, 11}
# объединение множеств
print(a | b)  # a.union(b)

# Разность множеств
print(a - b)  # a.difference(b)

# Пересечение множеств
print(a & b)  # a.intersection(b)

# Симметричная разность множеств
print(a ^ b)  # a.symmetric_difference(b)

