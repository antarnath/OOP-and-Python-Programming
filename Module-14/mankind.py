class Human:
    def __init__(self, gender, height, weight):
        self.gender = gender 
        self.height = height
        self.weight = weight

class Police(Human):
    def __init__(self, gender, height, weight, cases, nationality):
        super().__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality

class CsEngineering(Human):
    def __init__(self, gender, height, weight, love_to_code, has_gf):
        super().__init__(gender, height, weight)
        self.love_to_code = love_to_code
        self.has_gf = has_gf

if __name__ == "__main__":
    police = Police("male", 84, 64, True, "Bangladeshi")
    print(police.height)

    eng = CsEngineering("male", 84, 64, True, False)
    print(eng.has_gf)

    eng2 = CsEngineering(height=70, weight=65, gender="male", has_gf=True, love_to_code=False)
    print(eng2.weight)