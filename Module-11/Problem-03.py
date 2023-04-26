s = "Programming Hero is the best"
new_str = ""
temp = ""
for val in s:
    if val!=' ':
        temp = val+temp
    else:
        new_str += temp+" "
        temp = ""
new_str += temp
print(new_str)