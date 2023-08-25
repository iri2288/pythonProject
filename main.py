# Функции с переменным числом аргументов
# * сообщает интерпритатору что кол-во позиционных аргументов будет переменным >0 передается кортеж
# ** сообщает интерпритатору что кол-во именованных аргументов будет переменным >0 передается словарь
def var_args(*args):
    """
    :param args: только целые числа,
    :return: кортеж - число аргументов и сумму как целое число
    """
    summ = 0
    for arg in args:
        summ += arg
    # return(var_args(1, 2, 3, 4, 5)
    return len(args), summ, args  # возврат нескольких значений кортеж

gnt, summa, lst = var_args(1, 2, 3, 4, 5)
print('Число аргументов:', gnt)
print('Сумма:', summa)
print('Числа на входе:', *lst)


def named_args(**kwargs):  # keyword именованные
    print(kwargs)


# вызов named_args (key-word)
named_args(first='первый', second='второй', third='третий')  # создается словарь


def any_func_refer(n):
    n[0] = 0
    print(n)


array = [5, 25, 625]
any_func_refer(array)
