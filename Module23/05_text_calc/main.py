def is_okay(line):
    line = line.split()
    if len(line) != 3:
        raise SyntaxError
    o1, s, o2 = int(line[0]), line[1], int(line[2])
    if s not in ('+', '-', '*', '/', '//', '%', '**'):
        raise NameError
    if s == '+':
        return o1 + o2
    elif s == '-':
        return o1 - o2
    elif s == '*':
        return o1 * o2
    elif s == '/':
        return o1 / o2
    elif s == '//':
        return o1 // o2
    elif s == '%':
        return o1 % o2
    else:
        return o1 ** o2


total_sum = 0
try:
    with open('calc.txt', 'r') as r_f:
        for i_line in r_f:
            try:
                res = is_okay(i_line)
            except ValueError:
                print('Операнды должны быть целыми числами! исправьте -> ', i_line.strip())
            except SyntaxError:
                print('Тут чего-то не хватает -> ', i_line.strip())
            except NameError:
                print('Операция должна быть известна нам и компьютеру -> ', i_line.strip())
            except ZeroDivisionError:
                print('Произошло деление на 0, так нельзя -> ', i_line.strip())
            else:
                print(i_line.strip() + ' = ' + str(res))
                total_sum += res
except FileNotFoundError:
    print('В файле нет никаких выражений :(')
finally:
    print('Общая сумма результатов: ', total_sum)
