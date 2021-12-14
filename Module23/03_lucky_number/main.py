import random

errors = (BaseException, KeyboardInterrupt, StopIteration, AssertionError, ImportError, UnboundLocalError,
          InterruptedError, ReferenceError, TypeError, Warning)
total_sum = 0
while True:
    num = int(input('Введите число: '))
    total_sum += num
    if random.randint(1, 13) == 13:
        raise random.choice(errors)('Случайное исключение')

    with open('file.txt', 'a') as w_f:
        w_f.write(str(num) + ' ')
    if total_sum >= 777:
        print('Сбор чисел окончен, спасибо)')
        break
