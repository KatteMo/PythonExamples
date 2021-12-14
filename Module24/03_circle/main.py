import math


class Circle:

    def __init__(self, x=0, y=0, r=1):
        # подскажите, пожалуйста, как здесь проверку покрасивее сделать ((
        if not (type(x) == int or type(x) == float and type(y) == int or type(y) == float and type(r) == int or type(
                r) == float):
            raise TypeError
        self.x = x
        self.y = y
        if r <= 0:
            raise ValueError
        self.r = r

    def get_square(self):
        print('Площадь = {:.3f}'.format(self.r ** 2 * math.pi))

    def get_perimeter(self):
        print('Периметр = {:.3f}'.format(2 * math.pi * self.r))

    def make_more(self, k):
        if k <= 1:
            print('Это не сделает круг больше, ты чего...')
        else:
            self.r *= k

    def is_crossing(self, c):
        if not isinstance(c, Circle):
            print('Для нахождения пересечения нужно передать вторую окружность')
        distance = math.sqrt((self.x - c.x) ** 2 + (self.y - c.y) ** 2)
        sum_r = c.r + self.r
        if distance < sum_r:
            print('Пересекаются')
        elif distance == sum_r:
            print('Касаются')
        else:
            print('Они находятся на расстоянии друг от друга')

    def info(self):
        print('Координаты: ({},{}); радиус = {}'.format(self.x, self.y, self.r))


try:
    c1 = Circle(1, 1, 5)
    c2 = Circle(2, 2, 7)
    c1.get_square()
    c2.get_perimeter()
    c2.make_more(5)
    c2.make_more(0.1)
    c1.info()

    # c31 = Circle('a', 1, 1)
    # c32 = Circle(1, 'a', 1)
    # c33 = Circle(1, 1, 'a')
    # c34 = Circle(1, 1, -3)

    c1.is_crossing(c2)
    c3 = Circle(7, 1, 1)
    c3.is_crossing(c1)
    c4 = Circle(22, 22, 1)
    c4.is_crossing(c1)
except TypeError:
    print('Ты чего вообще написал... нужны числа, цифры')
except ValueError:
    print('Как радиус может быть меньше 0? или Вам нужна точка?')
# отличные сообщения!
