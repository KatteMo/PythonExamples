import random


class Student:

    def __init__(self, fi, n, p):
        self.surname = fi
        self.number = n
        self.progress = p

    def info(self):
        print(self.surname, self.number, self.progress)

    def mid_b(self):
        b = 0
        for num in self.progress:
            b += num
        return b / 5


names_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numbers_ = [1, 2, 3, 4, 5, 4, 3, 2, 5, 4]
lst = [Student(names_[i], numbers_[i], [random.randint(1, 10) for _ in range(5)]) for i in range(10)]
scores = [i.mid_b() for i in lst]
sort_lst = []
for el in range(10):
    m_s = max(scores)
    ind = scores.index(m_s)
    scores[ind] = -1
    sort_lst.append(lst[ind])

print('\nbefore sorting')
for i in lst:
    i.info()
print('\nafter sorting')
for j in sort_lst:
    j.info()
