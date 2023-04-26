class methodes:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def pow(self):
        return pow(self.x, self.n)
    def sum(self):
        return self.x + self.n

anta = methodes(3, 3)
print(anta.sum())