class Person:
    def __init__(self, name, age, money, height=65):
        self.name = name
        self.age = age
        self.money = money
        self.height = height

    def __call__(self):
        print(f"This is {self.name} with age {self.age} and have {self.money}")
    def __len__(self):
        return self.height
    def __eq__(self, other):
        return self.age == other.age
    def __add__(self, other):
        return self.age + other.money

alim = Person("Alim", 15, 400)
dalim = Person("Dalim", 16, 500)

print(alim == dalim)
print(len(alim))