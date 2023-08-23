# словари
# список index - value
# словарь key - value
d = dict.fromkeys([1, 2, 3, 4, 5], '1')

print(d)

# используя два списка
keys = ['one', 'two', 'three']
values = ['один', 'два', 'три']
d = dict() # создан пустой словарь
l = len(keys)

# for i in range(l):
#    d.keys[i] = values[i]

d = {k: v for k, v in zip(keys, values)}  # генерация словаря с помощью zip

print(d)