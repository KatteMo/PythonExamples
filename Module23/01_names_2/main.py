count = 0
try:
    with open('people.txt', 'r') as r_f:
        for num, name in enumerate(r_f):
            name = name.strip()
            l = len(name)
            try:
                if l < 3:
                    with open('errors.log', 'a') as w_f:
                        w_f.write('In line number {} you have name {} - it is error\n'.format(num + 1, name[:l]))
                    raise BaseException
            except BaseException:
                print('В строчке номер {} менее 3 букв'.format(num + 1))
            else:
                count += l
except:
    print('Произошла какая-то ошибка')
print('Total sum:', count)
