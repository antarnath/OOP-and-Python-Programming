data =  input();
output=""
for character in data:
    output += chr((ord(character)+1-97)%26 + 97)

print(output)
