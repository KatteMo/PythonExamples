import random


class Human:

    def __init__(self, name, home, satiety=50):
        if not name.isalpha() or not isinstance(home, Home) or not type(satiety) == int:
            raise TypeError
        self.name = name
        self.home = home
        self.satiety = satiety

    def eat(self):
        if self.home.food > 0:
            self.home.food -= 1
            self.satiety += 1
            print(self.name, ': поели, было сытно')

    def work(self):
        if self.satiety >= 0:
            self.satiety -= 1
            self.home.money += 1
            print(self.name, ': поработали, устали')

    def play(self):
        if self.satiety >= 0:
            self.satiety -= 1
            print(self.name, ': поиграли')

    def go_for_food(self):
        if self.home.money > 0:
            self.home.money -= 1
            self.home.food += 1
            print(self.name, ': сгоняли за едой в магазин')

    def info(self):
        print('Имя:{}; Сытость:{}; Еда:{}; Деньги:{} '.format(self.name, self.satiety, self.home.food, self.home.money))


class Home:

    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money


def what_am_i_doing_now(someone):
    if not isinstance(someone, Human):
        raise ValueError
    num = random.randint(1, 6)
    if someone.satiety == 0 and someone.home.food == 0:
        print(someone.name, ': умерли смертью...')
        exit(0)
    if someone.satiety < 20 and someone.home.food > 0:
        someone.eat()
    elif someone.home.food < 10 and someone.home.money > 0:
        someone.go_for_food()
    elif someone.home.money < 50 and someone.satiety > 0:
        someone.work()
    elif num == 1:
        someone.work()
    elif num == 2:
        someone.eat()
    else:
        someone.play()


try:
    sweet_home = Home()
    man = Human('Мужик', sweet_home)
    woman = Human('Женщина', sweet_home)
    for i in range(1, 366):
        print('\nДень', i)
        what_am_i_doing_now(man)
        man.info()
        what_am_i_doing_now(woman)
        woman.info()
except TypeError:
    print('Что-то не то передали при объявлении')
except ValueError:
    print('В функцию о будущем нужен человек')
