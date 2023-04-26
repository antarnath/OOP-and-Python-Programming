str = input()
Uppercase=0
Lowercase=0
Digits=0
Symbol=0
for char in str:
    if(char>='a' and char<='z'):
        Lowercase+=1
    elif(char>='A' and char<='Z'):
        Uppercase+=1
    elif(char>='1' and char<='9'):
        Digits+=1
    else:
        Symbol+=1
print("UpperCase = ",Uppercase)
print("Lowercase = ",Lowercase)
print("Digits = ",Digits)
print("Symabol = ",Symbol)
