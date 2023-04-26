s1=input()
s2=input()

flag=True
for i in s1:
    check=False
    for j in s2:
        if i==j:
            check=True
    if check==False:
        print("False")
        flag=False
        break
if flag==True:
    print("True")