class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def info(self):
        print('у воина {} {} очков здоровья'.format(self.name, self.health))

    def hit(self, war):
        if not isinstance(war, Warrior):
            print('Нужно указать имя воина')
        else:
            war.health -= 20
            if war.health <= 0:
                print('Воин {} атаковал воина {} и победил его так как'.format(self.name, war.name), end=' ')
            else:
                print('Воин {} атаковал воина {} и теперь'.format(self.name, war.name), end=' ')
            war.info()


f = Warrior('first')
s = Warrior('second')
f.info()
s.info()

s.hit(f)
for _ in range(4):
    f.hit(s)
    s.hit(f)
