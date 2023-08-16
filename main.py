for i in range(101):
    if i % 10 == 5:
        print(i)

a = list()  # пустой список с помощью функции list

for i in range(101):
    if i % 10 == 5:
        a.append(i)

print(*a, sep=', ')  # * передача аргумента в виде списка

