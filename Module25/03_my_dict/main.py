class MyDict(dict):

    def get(self, key):
        if key in self.keys():
            return self[key]
        else:
            return 0


d = MyDict()
d[1] = 'one'
d[2] = 'two'
d[3] = 'three'
print(d.get(1))
print(d.get(3))
print(d.get(7))
