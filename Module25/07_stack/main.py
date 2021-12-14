class Stack:
    def __init__(self):
        self.__st = []

    def __str__(self):
        return '; '.join(self.__st)
        # return str(self.__st)

    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()

    def chek_elem(self, elem):
        if elem in self.__st:
            return True
        return False

    def del_el(self, el):
        if len(self.__st) == 1:
            self.__st.pop()
        else:
            self.__st.remove(el)

    def __len__(self):
        return len(self.__st)


class Manager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i in sorted(self.task.keys()):
                display.append('\n{} {}'.format(i, self.task[i]))
        return ''.join(display)

    def new_task(self, tsk, priority):
        for i in self.task:
            if self.task.get(i).chek_elem(tsk):
                print('Задачу, которую вы пытаетесь ввести уже есть - {}'.format(tsk))
                return
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(tsk)

    def rem_task(self, tsk):
        if len(self.task.keys()) == 0:
            print('\nEmpty manager')
            return
        for i in self.task:
            if self.task.get(i).chek_elem(tsk):
                if min(self.task.keys()) == i:
                    if len(self.task.get(i)) == 1:
                        self.task.pop(i)
                    else:
                        self.task.get(i).del_el(tsk)
                    print('мы убрали задачу - {}'.format(tsk))
                    break
                else:
                    print('не могу убрать {} - у него не самый высокий приоритет'.format(tsk))
                    break
        else:
            print('не могу убрать {} - этого нет в списке'.format(tsk))


man = Manager()
man.new_task('Сделать уборку', 4)
man.new_task('Помыть посуду', 4)
man.new_task('Отдохнуть', 1)
man.new_task('Поесть', 2)
man.new_task('Сделать дз', 2)
print(man)

# man.rem_task('Отдохнуть')
# print(man)
# man.rem_task('Поесть')
# print(man)
# man.rem_task('Сделать уборку')
# man.rem_task('Сделать дз')
# print(man)
#
# man.rem_task('Сделать уборку')
# print(man)
# man.rem_task('Помыть посуду')
# man.rem_task('dsd')
