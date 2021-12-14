class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Energy):
            return Flood()


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Energy):
            return Tornado()


class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Energy):
            return Ignition()


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Energy):
            return Earthquake()


class Energy:
    def __add__(self, other):
        if isinstance(other, Water):
            return Flood()
        elif isinstance(other, Earth):
            return Earthquake()
        elif isinstance(other, Fire):
            return Ignition()
        elif isinstance(other, Air):
            return Tornado()


class Storm:
    def __str__(self):
        return 'Вода + Воздух = Шторм\n'


class Steam:
    def __str__(self):
        return 'Вода + Огонь = Пар\n'


class Dirt:
    def __str__(self):
        return 'Вода + Земля = Грязь\n'


class Lightning:
    def __str__(self):
        return 'Воздух + Огонь = Молния\n'


class Dust:
    def __str__(self):
        return 'Воздух + Земля = Пыль\n'


class Lava:
    def __add__(self, other):
        if isinstance(other, Earthquake):
            return Eruption()

    def __str__(self):
        return 'Огонь + Земля = Лава\n'


class Flood:
    def __str__(self):
        return 'Вода + Энергия = Потоп\n'


class Ignition:
    def __str__(self):
        return 'Огонь + Энергия = Пожар\n'


class Tornado:
    def __str__(self):
        return 'Воздух + Энергия = Торнадо\n'


class Earthquake:
    def __add__(self, other):
        if isinstance(other, Lava):
            return Eruption()

    def __str__(self):
        return 'Земля + Энергия = Землетрясение\n'


class Eruption:
    def __str__(self):
        return 'Лава + Землетрясение = Извержение Вулкана\n'


a = Water()
b = Air()
c = Fire()
d = Earth()

res1 = a + b
res2 = a + c
res3 = a + d
res4 = b + c
res5 = b + d
res6 = c + d
r = d + d
print(res1, res2, res3, res4, res5, res6, r)

en = Energy()
r1 = a + en
r2 = en + b
r3 = c + en
r4 = en + d
print(r1, r2, r3, r4)

l = Lava()
ea = Earthquake()
rr = l + ea
print(rr)
