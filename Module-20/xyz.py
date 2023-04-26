lines = None
with open('test.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line + "  *antar*")
