list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

reversed(list2)
list2.reverse()

x = zip(list1,list2)
for i in x:
    print(i)