# Исключения try+exept / try+finally
# Модули и их применение
# Утверждения (Assertion) используется на момент отладки программы

try:
    text = input('Введите любой текст: ')
    assert len(text) > 3  # утверждение
except AssertionError:
    print('Длина текста меньше 3 символов')
