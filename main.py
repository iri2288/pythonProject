a = ['Первый', 'Второй']
members = 10

for x in (range(members)):
    print(a[x % 2])

print('Расчет окончен')


for x in range(11):
    a.append(x)

for index in range(0, len(a),2):
    print(a[index])


