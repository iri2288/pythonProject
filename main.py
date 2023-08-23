# список заполненный лишь четными числами от 2 до 10
a = [x for x in range(2,11) if x % 2 == 0]
print(a)

string = '128 256 512 767'
a = [int(x) for x in string.split()]
print(a)