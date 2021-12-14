board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-', ]


def info_board():
    print(' ' + ' | ' + '1' + ' | ' + '2' + ' | ' + '3')
    print('1' + ' | ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('2' + ' | ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('3' + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8])


def new_move(symb):
    print('\nход ' + symb)
    position = input('Введите желаемую позицию, 2 числа чере пробел -'
                     ' сначала номер строки, затем номер столбца: ').split()
    y = int(position[0]) - 1
    x = int(position[1]) - 1
    if not (0 <= x <= 2) or not (0 <= x <= 2):
        raise ValueError
    else:
        if board[y * 3 + x] != '-':
            raise TypeError
        board[y * 3 + x] = symb


def is_winner(board):
    combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))

    for i in combinations:
        if board[i[0]] == board[i[1]] == board[i[2]] != '-':
            return board[i[0]]
        if all(cell != '-' for cell in board):
            return 'Ничья'
    return None


lst_symb = {1: 'X', -1: 'O'}
flag = 1
while True:
    info_board()
    try:
        new_move(lst_symb[flag])
        cur_stat = is_winner(board)
        if cur_stat:
            if cur_stat == 'Ничья':
                print('Игра закончилась ничьей')
            else:
                print('Игрок {} победил! Поздравляю!'.format(cur_stat))
            break
    except ValueError:
        print('Не те числа ввели...')
    except TypeError:
        print('Место уже занято')
    else:
        flag *= -1
