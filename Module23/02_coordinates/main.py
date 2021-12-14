import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            x = int(nums_list[0])
            y = int(nums_list[1])
            res1 = f(x, y)
            try:
                res2 = f2(x, y)
                number = random.randint(0, 100)
            except ZeroDivisionError:
                raise SyntaxError  # не придумал как сделать так, чтобы вот тут кинуть ошибку и выйти
            else:
                with open('result.txt', 'a') as file_2:
                    my_list = sorted([res1, res2, number])
                    file_2.write(str(my_list) + '\n')

except ZeroDivisionError:
    print('В первой функции произошло деление на 0, поэтому программа завершена')
except ValueError:
    print('Невозможно привести координаты к числовому формату, проверьте входные данные')
except SyntaxError:
    print('Во второй функции произошло деление на 0')
except:
    print('Проблемка не опознана')
else:
    print('Результаты успешно записаны!')
