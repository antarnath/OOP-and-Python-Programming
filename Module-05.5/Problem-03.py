list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

list3 = []
for i, st in enumerate(list1):
    list3.append(list1[i]+list2[i])

print(list3)