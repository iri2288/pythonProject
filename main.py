# При наследовании
# базовый,

# __init__ - конструктор объектов
# __del__ - деструктор
class Student:
    def __init__(self, name, university):
        self.name = name
        self.university = university

# для print() и str()
# вывод читабельной информации об объекте
    def __str__(self):
        return f'{self.name}, {self.university}'


# для разработчика (debug) информация о сложном объекте, список объектов, кортеж и т.д.
    def __repr__(self):
        return f'Класс: {self.__class__.__name__}{self.name}, {self.university}'



student = Student('Bill', 'Oxford'), Student('John', 'Oxford')

print(student)
