# def square(x):
#     return x * x
square = lambda x: x*x

result = square(6)
# print(result)

add = lambda x, y: x + y
# print(add(10, 20))

numbers = [12, 45, 65, 23, 89, 78, 11]
def double_it(x):
    return x * 2

doubled_numbers = map(double_it, numbers)
# print(numbers)
# print(list(doubled_numbers))

doubled_numbers2 = map(lambda x: x * 2, list(doubled_numbers))
# print(list(doubled_numbers2))

bigger_numbers = filter(lambda num: num > 50, numbers)
# print(list(bigger_numbers))

actors = [
    {'name': 'sakib', 'age': 34},
    {'name': 'manna','age': 50},
    {'name':'sabana', 'age':65},
    {'name':'bubli', 'age':30}
    ]

senior_actors = filter(lambda actor: actor['age'] > 35, actors)
print(list(senior_actors))