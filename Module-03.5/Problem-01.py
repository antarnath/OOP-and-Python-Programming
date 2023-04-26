str = input("Any String ")
output=""
for char in str:
    if(char>='a' and char<='z'):
        output+=(chr(ord(char)-32))
    elif(char>='A' and char<='Z'):
        output+=(chr(ord(char)+32))
    else:
        output+=char
print(output)