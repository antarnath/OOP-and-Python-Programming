# class Item:
#     def __init__(self, itemName, itemPrice):
#         assert itemPrice > 0, f'Error line 3, {itemPrice} is invalid'
#         self.itemName = itemName
#         self.itemPrice = itemPrice


# item = Item("Plate", -150)
# print(item.itemName, item.itemPrice)

class Person:
    def __init__(self, name, phone, age):
        assert age > 13, f'Only geater than 13 is accepted'
        assert len(phone) == 11, f'Invalid phone number'
        self.name = name
        self.phone = phone
        self.age = age
    def __repr__(self):
        return f'{self.name}, {self.phone}, {self.age}'

antar = Person("Antar", '0178664433', 14)
print(antar)

