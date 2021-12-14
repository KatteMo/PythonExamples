class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class BedsOfPotato:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('\nКартошка растет')
        for i in self.potatoes:
            i.grow()

    def are_all_rape(self, flag=False):
        if not all([i.is_ripe() for i in self.potatoes]):
            if flag:
                return False
            print('Картошка еще не поспела!\n')
        else:
            if flag:
                return True
            print('Вся картошка созрела! Можно собирать!\n')


class Gardener:

    def __init__(self, name, bed):
        self.name = name
        self.bed = bed

    def care(self):
        self.bed.grow_all()

    def get_harvest(self):
        if not self.bed.potatoes:
            print('На грядках ничего не растет - собирать нечего')
        elif self.bed.are_all_rape(1):
            print('Урожай собран! можно сажать снова')
            self.bed.potatoes = []
        else:
            print('Еще рано собирать - не спелое еще')


m_g = BedsOfPotato(5)
g1 = Gardener('Ivan', m_g)
g1.care()
g1.care()
g1.get_harvest()
g1.care()
g1.get_harvest()
g1.get_harvest()
