# рекурсия на примере факториала в python глубина рекурсии 1000 шагов при обходе бинарного дерева


def factorial(x):
    if x == 1:
        return x
    return x * factorial(x - 1)

print(factorial(5))

def greeting(hour)

    """
    :param hour:  0-23
    :return: Доброе утро, день, вечер, ночь
    """