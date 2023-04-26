import csv

with open('./data/my_friends.csv', 'r') as file:
    lines = csv.reader(file, delimiter=True) 
    # header = next(lines)
    for line in lines:
        print(line)
    # print(header)

# import keyboard
# keyboard.read_key()

# if keyboard.is_pressed('-1'):
#     print("antar")