n = int(input())

lst = [[i for i in range(1,n+1, 1)] for j in range(1, 1+n, 1)]
for i in range(len(lst)):
    if i==0:
        pass
    else:
        for j in range(len(lst[i])):
            lst[i][j] = lst[i-1][j]
        tmp = lst[i][i]
        lst[i][i] = 1
        lst[i][i-1] = tmp

for list in lst:
    for val in list:
        print(val, end="")
    print()