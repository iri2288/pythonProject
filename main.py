# Переопределение
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return (self.a * self.b)
    def perimetr(self):
        return (self.a + self.b) * 2
    def __eq__(self, other):
        if (self.a = other.a) and (self.b = other.b)
            return True
        return False
    def __add__(self, other):
        return (self.a + other.a, self.b + other.b)

    def __divmod__(self, other):
        return (self.a / other.a, self.b / other.b)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = 'Квадрат'


rect1 = Rectangle(5,5)
rect2 = Rectangle(5,5)

if rect1 == rect2:  # сравниваем адреса объектов
    print('Они равны')
else:
    print('Они не равны')

 sq = sq1 + sq2
print(sq)




