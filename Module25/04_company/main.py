class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):

    def wages(self):
        pass


class Manager(Employee):
    __my_wages = 13000

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        # TODO если метод полностью повторяет родительский, то переопределять его не нужно

    def wages(self):
        return Manager.__my_wages


class Agent(Employee):
    __my_wages = 5000

    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.__sales = sales

    def wages(self):
        return Agent.__my_wages + 0.05 * self.__sales


class Worker(Employee):
    __my_wages = 100

    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.__hours = hours

    def wages(self):
        return Worker.__my_wages * self.__hours


m1, m2, m3 = Manager('a', 'aa', 11), Manager('b', 'bb', 22), Manager('c', 'cc', 33)
a1, a2, a3 = Agent('d', 'dd', 44, 2000), Agent('e', 'ee', 55, 3000), Agent('f', 'ff', 66, 4000)
w1, w2, w3 = Worker('g', 'gg', 77, 100), Worker('h', 'hh', 88, 200), Worker('i', 'ii', 99, 300)

lst = (m1, m2, m3, a1, a2, a3, w1, w2, w3)

for el in lst:
    print('ЗП определенной личности: ', el.wages())
