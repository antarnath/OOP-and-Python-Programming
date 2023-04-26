numbers = [12, 45, 65, 23, 89, 78, 11]
numbers_set = {12, 45, 56, 11, 12, 89}
numbers_tuple = 12, 45, 56, 45, 12, 89
marks = {'physics':12, 'chemistry':45, 'math':56,}
total = 0
for num in numbers:
    total += num
# print(total)

total=0 
for num in numbers_set:
    total += num
# print(total)

total=0
for num in numbers_tuple:
    total += num
# print(total)

total = 0
s = ""
for mark in marks:
    total += marks[mark]
# print(total)
# print(s)

for i, num in enumerate(numbers):
    print(i,num)
