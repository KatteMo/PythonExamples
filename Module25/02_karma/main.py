import random


class KillError(Exception):
    def __str__(self):
        return 'KillError'


class DrunkError(Exception):
    def __str__(self):
        return 'KillError'


class CarCrashError(Exception):
    def __str__(self):
        return 'KillError'


class GluttonyError(Exception):
    def __str__(self):
        return 'KillError'


class DepressionError(Exception):
    def __str__(self):
        return 'KillError'


def one_day():
    lst_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst_err = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
    num = random.choice(lst_num)
    if num < 10:
        return num % 7 + 1
    else:
        error = random.choice(lst_err)
        with open('karma.log', 'a') as w_f:
            w_f.write(str(error) + '\n')
            # почему-то метод __str__ не работает, либо я что-то не понимаю, ну а так вроде все остальное ок
            # в итоге в файл запишется некрасиво
        raise error


count = 0
while True:
    try:
        count += one_day()
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError):
        print('Произошел сбой по карме - сегодня ее не накапливали')
    if count >= 500:
        print('Накопили, хватит')
        break