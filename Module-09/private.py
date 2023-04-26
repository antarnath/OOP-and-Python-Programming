class User:
    def __init__(self, name, password, phone):
        self.name = name
        self.__password = password
        self.phone = phone

    def __get_password(self):
        print(self.__password)
        
Antar = User("Antar", "Anijarij", "01909531616")
# print(Antar.__password)
# print(Antar.phone)

Antar.get_password()