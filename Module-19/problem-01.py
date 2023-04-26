st = input()
st1 = ""
for i in range(len(st)-1,-1,-1):
    st1 += st[i]

if st == st1:
    print("palindrome")
else:
    print('not palindrome')