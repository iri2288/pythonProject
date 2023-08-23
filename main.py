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


