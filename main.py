print(dir(''))
# Методы строк
# strip
# split
# join
# count

s = 'Мама мыла раму'

lst = s.split()  # пробел по умолчанию
print(type(lst))

string = ', ' .join(lst)

print(string)

lst = ['Козерог', 1]  # Козерог -1
# print(lst[0])

# new_lst = list(map(str, lst))
#print(new_lst)
# print('-'.join(list))

print('-'.join(map(str, lst)))
# print(str(num)[::-1])
# num = list(num)
# print(num)


