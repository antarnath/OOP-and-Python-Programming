largest = max(45, 89, 54, 116, -12)
# print(largest)
numbers = [12, 45, 65, 23, 89, 78, 11]
big_nums = max(numbers)
print(big_nums)
reverse_numbers = reversed(numbers)
# print(list(reverse_numbers))
sorted_numbers = sorted(numbers)
# print(sorted_numbers)

actors = [
    {'name': 'Sakib Khan', 'age': 34},
    {'name': 'xalma Khan', 'age': 54},
    {'name': 'ehahruk Khan', 'age': 52},
    {'name': 'bolaiman Khan', 'age': 23},
    {'name': 'cAmir Khan', 'age': 49},
    {'name': 'Asif Khan', 'age': 29}
]

sorted_actors = sorted(actors, key=lambda actor: actor['name'])
print(sorted_actors)