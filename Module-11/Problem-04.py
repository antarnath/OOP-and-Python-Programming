string = input("Input : ")
new_string=""
length = len(string)
for i in range(0, length, 2):
    for j in range(0,int(string[i+1])):
        new_string += string[i]
        
upper_str = ""
for val in new_string:
    if val>='A' and val<='Z':
        if val in upper_str:
            pass
        else:
            upper_str += val

new_string = sorted(new_string.lower())

string = ""
for val in new_string:
    if val.upper() in upper_str:
        string += val.upper()
    else:
        string += val
        
print(string)
