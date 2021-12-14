import math


class Car:

    def __init__(self, x, y, alpha):
        self.__x = x
        self.__y = y
        self.__alpha = math.radians(alpha % 360)

    def move(self, distance):  # будем предполагать что расстояние в км
        self.__x = math.sin(self.__alpha) * distance + self.__x
        self.__y = math.cos(self.__alpha) * distance + self.__y

    def new_alpha(self, betta):
        self.__alpha = betta

    def info(self):
        print('Координаты машины: x: {:.3f}'.format(self.__x), ' y: {:.3f}'.format(self.__y))

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_alpha(self):
        return self.__alpha

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_alpha(self, alpha):
        self.__alpha = alpha


class Bus(Car):
    price = 0
    total_distance = 0

    def __init__(self, x, y, alpha):
        super().__init__(x, y, alpha)
        self.__passengers = 0
        self.__money = 0

    def get_on_the_bus(self):
        self.__passengers += 1

    def get_off_the_bus(self):
        self.__passengers -= 1

    def move(self, distance):
        self.set_x(math.sin(self.get_alpha()) * distance + self.get_x())
        self.set_y(math.cos(self.get_alpha()) * distance + self.get_y())
        if distance <= 100:
            self.price = 300
        elif distance <= 500:
            self.price = 300 * 1.5
        else:
            self.price = 300 * 2
        self.total_distance += distance
        self.__money += self.__passengers * self.price

    def info(self):
        print('Сегодня проехали {} км и заработали {} рублей. Сейчас в салоне {} человек'.format(
            self.total_distance, self.__money, self.__passengers))


car = Car(0, 0, 420)
car.move(10)
car.info()

bus = Bus(0, 0, 120)
bus.get_on_the_bus()
bus.new_alpha(60)
bus.move(50)
bus.move(450)
bus.get_on_the_bus()
bus.info()
bus.move(550)
bus.get_off_the_bus()
bus.info()