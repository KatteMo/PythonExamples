name = input('Введите свое имя: ')
while True:
    print('\n1 - Посмотреть текущий текст чата\n2 - Отправить сообщение')
    answer = input('Ваш ответ(1 или 2): ')
    if answer == '1':
        try:
            with open('chat.txt', 'r') as r_f:
                print(''.join(r_f.readlines()))
        except FileNotFoundError:
            print('Пока что нет сообщений')
    elif answer == '2':
        message = input('Введите ваше сообщение: ')
        with open('chat.txt', 'a') as w_f:
            w_f.write('{name}: {message}'.format(name=name, message=message))
    else:
        print('Неизвестная программа!')
