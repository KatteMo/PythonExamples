class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        pass


class Apartment(Property):
    __tax = 1 / 1000

    def __init__(self, worth):  # TODO если метод полностью повторяет родительский, то переопределять его не нужно
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth * Apartment.__tax


class Car(Property):
    __tax = 1 / 200

    def __init__(self, worth):  # TODO здесь и далее см. комментарий выше
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth * Car.__tax


class CountryHouse(Property):
    __tax = 1 / 500

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth * CountryHouse.__tax


class User():

    def __init__(self, money, a_price, c_price, ch_price):
        self.__money = money
        self.__a_price = Apartment(a_price)
        self.__c_price = Car(c_price)
        self.__ch_price = CountryHouse(ch_price)

    def tax_info(self):
        a_tax = self.__a_price.tax_calculation()
        c_tax = self.__c_price.tax_calculation()
        ch_tax = self.__ch_price.tax_calculation()
        print('Налог на квартиру — {}, на машину — {}, на дачу — {}'.format(
            a_tax, c_tax, ch_tax))
        total_tax = a_tax + ch_tax + c_tax
        balance = self.__money - total_tax
        if balance >= 0:
            print('Общая сумма налогов {}, Вы сможете ее выплатить, еще останется {}'.format(total_tax, balance))
        else:
            print('Общая сумма налогов {}, Вы не сможете ее выплатить, не хватает {}'.format(total_tax, balance * -1))


m = int(input('Введите кол-во Ваших денег: '))
a = int(input('Введите стоимость Вашей квартиры: '))
c = int(input('Введите стоимость Вашей машины: '))
ch = int(input('Введите стоимость Вашей дачи: '))
man = User(m, a, c, ch)
man.tax_info()
