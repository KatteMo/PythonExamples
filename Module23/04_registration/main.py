def is_right(line):
    parts = line.split()
    if len(parts) != 3:
        raise ValueError
    else:
        name , mail, age = parts[0], parts[1], parts[2]
        if not name.isalpha():
            raise NameError
        elif '@' not in mail and '.' not in mail:
            raise SyntaxError
        elif not age.isdigit() or not (10 < int(age) < 99):
            raise ValueError


with open('registrations.txt', 'r', encoding='utf-8') as r_f:
    for i_line in r_f:
        try:
            is_right(i_line)
        except ValueError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as bw_f:
                bw_f.write(i_line[:len(i_line) - 1] + ' - ValueError\n')
        except NameError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as bw_f:
                bw_f.write(i_line[:len(i_line) - 1] + ' - NameError\n')
        except SyntaxError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as bw_f:
                bw_f.write(i_line[:len(i_line) - 1] + ' - SyntaxError\n')
        else:
            with open('registrations_good.log', 'a', encoding='utf-8') as gw_f:
                gw_f.write(i_line)