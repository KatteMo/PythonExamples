class Parent:

    def __init__(self, name, age, children):
        if not isinstance(age, int) or not isinstance(children, list) or not name.isalpha():
            raise TypeError
        self.name = name
        self.age = age
        for ch in children:
            if self.age - ch.age < 16:
                raise ValueError
        self.children = children

    def info_parent(self):
        print('Меня зовут {}, мне {} лет/года и вот мои дети: '.format(self.name, self.age))
        for ch in self.children:
            print('{} - {} лет/года, он сейчас {} и кстати {}'.format(
                ch.name, ch.age, Child.states[ch.calmState], Child.hungry_or_not[ch.isHungry]))

    def make_calm(self, ch):
        if isinstance(ch, Child):
            if ch in self.children:
                ch.calmState = True
                print('Ребенок успешно успокоен! можно спать :)')
            else:
                print('Это конечно ребенок, но не этого родителя :(')
        else:
            print('Чтобы успокоить ребенка, нужен ребенок...')

    def give_food(self, ch):
        if isinstance(ch, Child):
            if ch in self.children:
                ch.isHungry = False
                print('Ребенок успешно покормлен! :)')
            else:
                print('Это конечно ребенок, но не этого родителя :(')
        else:
            print('Чтобы покормить ребенка, нужен ребенок...')


class Child:

    def __init__(self, name, age, calmState=False, isHungry=True):
        if not isinstance(age, int) or not name.isalpha():
            raise TypeError
        self.name = name
        self.age = age
        self.calmState = calmState
        self.isHungry = isHungry

    states = {False: 'кричит - орёт', True: 'лежит - спит'}
    hungry_or_not = {False: 'уже поел, но это ненадолго', True: 'еще не ел и это надо исправлять'}


try:
    c1 = Child('a', 12)
    c2 = Child('b', 15)
    p1 = Parent('A', 88, [c1, c2])

    p1.info_parent()
    p1.make_calm(c1)
    p1.give_food(c2)
    p1.info_parent()

    p2 = Parent('B', 35, [c1])
    # p2 = Parent('B', 22, [c1])
    # p2.make_calm(5)
except ValueError:
    print('У ребенка и родителя не может быть разница меньше 16 лет (по закону так)')
except (TypeError, AttributeError):
    print('Неправильные данные при объявлении ребенка или родителя')
