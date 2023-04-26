sample_dict = {'a': 100, 'b': 200, 'c': 300}

flag = False
for key, value in sample_dict.items():
    if value==100:
        flag = True

if flag:
    print("present")
else:
    print("not present")