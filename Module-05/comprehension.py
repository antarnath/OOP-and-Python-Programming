numbers = [12, 45, 65, 23, 89, 78, 11]

odd_numbers = filter(lambda x: x%2!=0, numbers)
# print(list(odd_numbers))

odd_numbers2 = [num for num in numbers if num%2 == 1 and num%5==0]
print(odd_numbers2)