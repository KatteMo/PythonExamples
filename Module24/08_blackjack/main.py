import random


class SimpleCards:
    cards = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

    def ret_card(self, c):
        return [c, self.cards[c]]


class CardsWithPic:

    def __init__(self):
        self.val = {'Валет': 10, 'Дама': 10, 'Король': 10}

    def ret_card(self, c):
        return [c, self.val[c]]


class Ace:

    def __init__(self):
        self.val = ['Туз', 11]

    def ret_card(self):
        return self.val


class Cards:
    simple_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    cards_with_pic = ['Валет', 'Дама', 'Король']

    def what_card(self, num):
        if num in self.simple_cards:
            return SimpleCards().ret_card(num)
        elif num == 14:
            return Ace().ret_card()
        else:
            return CardsWithPic().ret_card(self.cards_with_pic[num - 11])


def first_cards(nums):
    rand_num1 = random.choice(nums)
    ind1 = nums.index(rand_num1)
    number_for_searching1 = nums.pop(ind1)
    first_card = Cards().what_card(number_for_searching1)

    rand_num2 = random.choice(nums)
    ind2 = nums.index(rand_num2)
    number_for_searching2 = nums.pop(ind2)
    second_card = Cards().what_card(number_for_searching2)
    return [first_card, second_card]


def next_cards(nums):
    rand_num = random.choice(nums)
    ind = nums.index(rand_num)
    number_for_searching = nums.pop(ind)
    card = Cards().what_card(number_for_searching)
    return card


def is_ace(cards):
    for couple in cards:
        if 'Туз' in couple:
            return True


def info_h(obj, count):
    print('\nКарты на руках у игрока: ', end=' ')
    for i in obj:
        print(i[0], '-', i[1], end=', ')
    print('- Сумма их значений:', count)


def info_k(obj, count):
    print('Карты на руках у компьютера: ', end=' ')
    for i in obj:
        print(i[0], '-', i[1], end=', ')
    print('- Сумма их значений:', count)


nums_h = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums_k = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
h = first_cards(nums_h)
k = first_cards(nums_k)
dead_line = 21
counter = [0, 0]

for i in h:
    counter[0] += i[1]

for j in k:
    counter[1] += j[1]

while True:
    count_h = counter[0]
    if count_h > dead_line:
        if is_ace(h):
            for c in h:
                if c[0] == 'Туз':
                    c[1] = 1
                    counter[0] -= 10
                    continue
        else:
            print('\n Игрок проиграл ------')
            info_h(h, count_h)
            break

    info_h(h, count_h)
    answ = input('Будет ли брать еще игрок? (да или нет): ')
    if answ == 'нет':
        count_k = counter[1]
        if count_h > count_k:
            print('Игрок выиграл!!!')
        elif count_h < count_k:
            print('Компьютер выиграл!!!')
        else:
            print('Ничья')
        break
    if answ == 'да':
        curr = next_cards(nums_h)
        h.append(curr)
        counter[0] += curr[1]

info_k(k, counter[1])
