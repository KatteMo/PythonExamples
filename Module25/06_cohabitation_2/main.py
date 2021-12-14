import random
import numpy


class Pet:

    def __init__(self, name, home):
        if not name.isalpha() or not isinstance(home, Home):
            raise TypeError
        self.home = home
        self.name = name
        self.satiety = 30


class People:  # NOTE точнее будет назвать этот класс Human (человек), а не People (люди)
    total_food = 0
    total_money = 0
    coat_count = 0

    def __init__(self, name, home):
        if not name.isalpha() or not isinstance(home, Home):
            raise TypeError
        self.name = name
        self.home = home
        self.satiety = 30
        self.happiness = 100

    def pet_cat(self):
        self.satiety -= 10
        self.happiness += 5
        print('Погладили кота')

    def info(self):
        print('{}: уровень сытости равен {} и счастья {}'.format(
            self.name, self.satiety, self.happiness))

    def eat(self):
        self.satiety += 10
        self.home.food -= 10
        self.total_food += 10
        print('Поели')

    def buy_food(self):
        self.home.food += 10
        self.home.money -= 10
        print('Купили еды')

    def buy_feed(self):
        self.home.feed += 10
        self.home.money -= 10
        print('Купили корма')

    def stats(self):
        print('\nБыло заработано денег - {}, съедено еды - {}, куплено шуб - {}'.format(
            self.total_money, self.total_food, self.coat_count))


class Home:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.feed = 30
        self.dirt = 0

    def new_dirt(self):
        self.dirt += 5

    def info(self):
        print('Дома {} грязи, {} денег, {} еды и {} корма'.format(
            self.dirt, self.money, self.food, self.feed))


class Husband(People):

    def work(self):
        self.satiety -= 10
        self.home.money += 150
        self.total_money += 150
        print('Муж работал')

    def play_computer(self):
        self.satiety -= 10
        self.happiness += 20
        print('Муж играл')


class Wife(People):

    def clean_house(self):
        self.satiety -= 10
        self.home.dirt -= 100
        self.home.dirt *= numpy.sign(self.home.dirt)
        print('Жена убирает дом')

    def buy_coat(self):
        self.satiety -= 10
        self.coat_count += 1
        self.happiness += 60
        self.home.money -= 350
        print('Решила купить шубу....')


class Cat(Pet):

    def eat(self):
        self.satiety += 10
        self.home.feed -= 10

    def sad_wallpaper(self):
        self.home.dirt += 5
        print('Кот подрал обои')

    def info(self):
        print('Мяу(имя) - {}, мяу(сытость) - {}'.format(self.name, self.satiety))


def what_is_husband_doing_now(h):
    if not isinstance(h, Husband):
        raise ValueError
    if h.satiety == 0 and h.home.food == 0 or h.happiness < 10:
        print(h.name, ': умер смертью...')
        exit(0)

    if h.home.dirt > 90:
        h.happiness -= 10
    if h.satiety <= 10 and h.home.food > 0:
        h.eat()
    elif h.home.food <= 10 and h.home.money > 0:
        h.buy_food()
    elif h.home.feed <= 10 and h.home.money > 0:
        h.buy_feed()
    elif h.home.money < 90 and h.satiety > 0:
        h.work()
    elif h.happiness < 30 and h.satiety > 0:
        h.play_computer()
    elif h.home.money < 200:
        h.work()
    else:
        h.pet_cat()


def what_is_wife_doing_now(w):
    if not isinstance(w, Wife):
        raise ValueError
    if w.satiety == 0 and w.home.food == 0 or w.happiness < 10:
        print(w.name, ': умерла смертью...')
        exit(0)

    if w.home.dirt > 100:
        if w.satiety > 10:
            w.clean_house()
        else:
            w.happiness -= 10
    if w.satiety <= 10 and w.home.food > 0:
        w.eat()
    elif w.home.food <= 10 and w.home.money > 0:
        w.buy_food()
    elif w.home.feed <= 10 and w.home.money > 0:
        w.buy_feed()
    elif w.happiness < 30 and w.satiety > 0 and w.home.money > 400:
        w.buy_coat()
    else:
        w.pet_cat()


def what_is_cat_doing_now(c):
    if not isinstance(c, Cat):
        raise ValueError
    if c.satiety == 0 and c.home.feed == 0:
        print(c.name, ': отправился в лучшую семью...')
        exit(0)

    num = random.randint(1, 3)
    if c.satiety <= 10 and c.home.feed > 0:
        c.eat()
    elif num == 2:
        c.satiety -= 10
        c.sad_wallpaper()


try:
    # шубы для счастья в моей программе не нужны видимо :)
    # с ребенком механику понял, но добавлять не буду, думаю
    sweet_home = Home()
    man = Husband('Мужик', sweet_home)
    woman = Wife('Женщина', sweet_home)
    cat = Cat('Кот', sweet_home)

    for i in range(1, 366):
        print('\nДень', i)
        what_is_wife_doing_now(woman)
        woman.info()
        what_is_husband_doing_now(man)
        man.info()
        what_is_cat_doing_now(cat)
        cat.info()
        sweet_home.new_dirt()
        sweet_home.info()

    man.stats()
except TypeError:
    print('Что-то не то передали при объявлении')
except ValueError:
    print('В функцию о будущем нужен определенный человек или кот')
