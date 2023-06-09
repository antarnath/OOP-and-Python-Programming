class User:
    def __init__(self, f_name, l_name):
        
        self.first = f_name
        self.last = l_name
        self.email = f"{self.first}.{self.last}@user.com"
    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, value):
        first, last = value.split(" ")
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@user.com"
    @full_name.deleter  
    def full_name(self):
        del self.first
        del self.last
    @property
    def get_email(self):
        return self.email
        
    def get_email(self):
        return self.email
    
mark = User("mark", "zuku")
print(mark.first)
print(mark.last)
print(mark.get_email())
print(mark.full_name)
mark.full_name = "Antar Nath"
print(mark.full_name)
print(mark.email)
print(mark.first)

print(mark.email)
# print(mark.full_name)