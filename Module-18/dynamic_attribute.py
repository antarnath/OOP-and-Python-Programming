class Item:
    all = []
    def __init__(self, itemName, itemPrice):
        self.__itemName = itemName
        self.__itemPrice = itemPrice
        self.all.append(self)

    def __repr__(self):
        return f'Item({self.itemName}, {self.itemPrice})'

item1 = Item('Bowl', 100)
item2 = Item('plate', 150)
item1._Item__discount = 10
# print(item1.__discount)
item1._Item__itemName = 'Bowl Broken'
print(item1._Item__itemName)

print(item1.__dict__)



