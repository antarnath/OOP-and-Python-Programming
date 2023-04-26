numbers = [12, 45, 56, 11, 12, 89]
# print(numbers)
numbers_set = {12, 45, 56, 11, 12, 89}
# print(numbers_set)
numbers_set.add(76)
numbers_set.add(45)
# print(numbers_set)
numbers_set.remove(11)
# print(numbers_set)
# print(len(numbers_set))
a = set("abcdefghij")
b = set("abdfgimnop")
print(a^b)