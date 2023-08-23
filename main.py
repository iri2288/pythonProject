# словари
# список index - value
# словарь key - value
d = dict()  # создание пустого словаря
d = {}  # создание пустого словаря
d = {
    'стол': 'table',
    'стул': 'chair',
}

d['вишня'] = 'cherry'

d = {
    'well': ['хорошо', 'колодец'],
    'блюдо' : 'окрошка'
    'состав': ['квас', 'яйцо', 'огурец', 'колбаса']
}

for item in d:
    if isinstance(type(d[item] == list))
        print(item, end=':\n')
        for v in d[item]:
        print('\t', v)
    else:
        print(item, d[item])

print(d['стол'])

for item in d:  # перебор словаря по ключам
    if isinstance(type(d[item] == list))
        d[item].sort()  # сортируем список перед выводом
        print(item, end=':\n')
        for v in enumerate(d[item)]:
        print('\t' + str(i+1) + '.', v)
    else:
        print(item, d[item], sep=': ')



print(d['стол'])
print(list(d.keys())) # список ключей
print(list(d.values())) # список значений
print(d.items())
# выясним есть ли слово "кот" среди ключей
if 'кот' in d.keys(): # метод keys - ключи
    print('Кот есть')

if 'cat' in d.values(): # метод values - значения
    print('Cat есть')

for x, y in d.items():
    print(x, y, sep='->')



